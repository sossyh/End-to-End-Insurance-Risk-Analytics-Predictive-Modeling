import pandas as pd
import numpy as np
from scipy import stats

class InsuranceHypothesisTester:
    def __init__(self, data):
        """Initialize with insurance data"""
        self.data = data.copy()
        self._preprocess_data()
        
    def _preprocess_data(self):
        """Clean and preprocess the data"""
        # Convert TotalClaims and TotalPremium to numeric, handling errors
        self.data['TotalClaims'] = pd.to_numeric(self.data['TotalClaims'], errors='coerce')
        self.data['TotalPremium'] = pd.to_numeric(self.data['TotalPremium'], errors='coerce')
        
        # Create binary claim indicator
        self.data['HasClaim'] = (self.data['TotalClaims'] > 0).astype(int)
        
        # Calculate margin
        self.data['Margin'] = self.data['TotalPremium'] - self.data['TotalClaims']
        
    def _proportions_ztest(self, count, nobs):
        """Custom z-test for proportions using scipy"""
        p1 = count[0] / nobs[0]
        p2 = count[1] / nobs[1]
        p_pooled = (count[0] + count[1]) / (nobs[0] + nobs[1])
        
        se = np.sqrt(p_pooled * (1 - p_pooled) * (1/nobs[0] + 1/nobs[1]))
        z = (p1 - p2) / se
        pval = 2 * (1 - stats.norm.cdf(abs(z)))  # Two-tailed test
        return z, pval
        
    def test_province_risk(self):
        """Test H₀: There are no risk differences across provinces"""
        provinces = self.data['Province'].unique()
        if len(provinces) < 2:
            return "Insufficient provinces for comparison"
            
        # For claim frequency (proportion with claims)
        freq_results = {}
        severity_results = {}
        
        # Compare each province to all others combined
        for province in provinces:
            province_data = self.data[self.data['Province'] == province]
            other_data = self.data[self.data['Province'] != province]
            
            # Claim frequency test
            count = [province_data['HasClaim'].sum(), other_data['HasClaim'].sum()]
            nobs = [len(province_data), len(other_data)]
            zstat, pval = self._proportions_ztest(count, nobs)
            freq_results[province] = pval
            
            # Claim severity test (only for policies with claims)
            if province_data['HasClaim'].sum() > 0 and other_data['HasClaim'].sum() > 0:
                tstat, pval = stats.ttest_ind(
                    province_data[province_data['HasClaim'] == 1]['TotalClaims'],
                    other_data[other_data['HasClaim'] == 1]['TotalClaims'],
                    equal_var=False
                )
                severity_results[province] = pval
        
        return {
            'claim_frequency': freq_results,
            'claim_severity': severity_results
        }
        
    # [Rest of your methods remain the same...]
    # Keep all other methods unchanged from your original implementation
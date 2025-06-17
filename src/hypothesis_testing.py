from scipy.stats import ttest_ind

def test_hypotheses(df):
    results = {}

    # Prepare claims per policy (assuming 'TotalClaims' is count of claims per row)
    claims_per_policy = df.groupby("PolicyID")["TotalClaims"].sum().reset_index(name="NumClaims")
    df = df.merge(claims_per_policy, on="PolicyID", how="left")

    # H1: Male vs Female average claims
    male_claims = df[df["Gender"] == "Male"]["NumClaims"]
    female_claims = df[df["Gender"] == "Female"]["NumClaims"]
    t1, p1 = ttest_ind(male_claims.dropna(), female_claims.dropna(), equal_var=False)
    results["H1_Male_vs_Female_NumClaims"] = {"p_value": p1, "reject": p1 < 0.05}

    # H2: Older (<2010) vs Newer (>=2010) vehicle average premium
    old_vehicle_premium = df[df["RegistrationYear"] < 2010]["TotalPremium"]
    new_vehicle_premium = df[df["RegistrationYear"] >= 2010]["TotalPremium"]
    t2, p2 = ttest_ind(old_vehicle_premium.dropna(), new_vehicle_premium.dropna(), equal_var=False)
    results["H2_Old_vs_New_Vehicle_TotalPremium"] = {"p_value": p2, "reject": p2 < 0.05}

    return results

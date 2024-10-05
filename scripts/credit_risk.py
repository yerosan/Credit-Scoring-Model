# src/credit_risk.py

class CreditRisk:
    """
    This class encapsulates the foundational aspects of understanding credit risk, 
    including reading materials and summaries of important concepts.
    """

    def __init__(self):
        self.references = {
            "Statistica Reference": "https://www3.stat.sinica.edu.tw/statistica/oldpdf/A28n535.pdf",
            "HKMA Alternative Credit Scoring": "https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/alternative_credit_scoring.pdf",
            "World Bank Credit Scoring Guidelines": "https://thedocs.worldbank.org/en/doc/935891585869698451-0130022020/original/CREDITSCORINGAPPROACHESGUIDELINESFINALWEB.pdf",
            "Towards Data Science Credit Risk Modeling": "https://towardsdatascience.com/how-to-develop-a-credit-risk-model-and-scorecard-91335fc01f03",
            "Credit Risk in Finance": "https://corporatefinanceinstitute.com/resources/commercial-lending/credit-risk/"
        }

    def summarize_basel_ii(self):
        """Provides a summary of the Basel II Capital Accord for credit risk."""
        summary = (
            "Basel II Capital Accord is an international banking regulation that requires financial institutions "
            "to maintain sufficient capital to cover their risks. It focuses on three pillars: "
            "1) Minimum capital requirements, 2) Supervisory review, and 3) Market discipline. "
            "For credit risk, financial institutions must evaluate borrower risk accurately to avoid default."
        )
        return summary

    def list_references(self):
        """Returns a list of key references for understanding credit risk."""
        return self.references


if __name__ == "__main__":
    credit_risk = CreditRisk()
    print("Summary of Basel II Capital Accord:")
    print(credit_risk.summarize_basel_ii())
    
    print("\nKey References for Understanding Credit Risk:")
    for name, url in credit_risk.list_references().items():
        print(f"{name}: {url}")

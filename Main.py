import Predictive_Analysis_Classification
import clean
import Clustering_Associationrules
import t_test
if __name__ == '__main__':
    # Basic Statistical Analysis and data cleaning insight Part
    print("##############################################")
    print("# Basic Statistical Analysis and data cleaning insight Part")
    print("##############################################")
    clean.main()
    # Cluster and Association Rule Part
    print("##############################################")
    print("# Cluster and Association Rule Part")
    print("##############################################")
    Clustering_Associationrules.execute()
    # Predictive_Analysis_Hypothesis_Test Part
    print("##############################################")
    print("# Predictive_Analysis_Hypothesis_Test Part")
    print("##############################################")
    t_test.execute()
    # Predictive_Analysis_Classification Part
    print("##############################################")
    print("# Predictive_Analysis_Classification Part")
    print("##############################################")
    Predictive_Analysis_Classification.execute()

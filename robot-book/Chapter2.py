import gtsam

#VARIABLES = Variables()
categories = ["cardboard", "paper", "can", "scrap metal", "bottle"]
# Category = VARIABLES.discrete("Category", categories)

Category = 0,5

category_prior = gtsam.DiscreteDistribution(Category, "200/300/250/200/50")
print(category_prior.pmf)
print("P('can'): ",category_prior(categories.index("can")))

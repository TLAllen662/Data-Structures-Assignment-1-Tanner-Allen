from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []


response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()

print(customer_preferences)

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)



# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"])
    })




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_preferences):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_preferences (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        match_count = count_matches(product["tags"], customer_preferences)
        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })

    return sorted(recommendations, key=lambda product: product["matches"], reverse=True)



# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_preferences)
print("Recommended Products:")
for recommendation in recommendations:
    print(f"- {recommendation['name']} ({recommendation['matches']} match(es))")




# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# This program uses loops, list operations, set conversion, set intersections, and
# sorting. The while loop collects preferences until the customer enters N. A list
# works well during input because values can be appended and their entry order is
# preserved. The list is then converted to a set, which removes duplicate preferences
# and makes comparisons efficient. A second loop processes every product and builds a
# new list of dictionaries. It keeps each product name while converting its tag list
# into a set.
#
# The count_matches function uses set intersection to find tags shared by a product
# and the customer. The length of that intersection becomes the match score. This is
# simpler and more efficient than manually comparing every tag combination. The
# recommendation function calculates a score for each product, removes products with
# zero matches, and sorts the remaining products from the highest score to the lowest.
# 2. How might this code change if you had 1000+ products?
# With 1,000 or more products, scanning the entire catalog for every customer could
# become slower. I could build an index mapping each tag to the products that contain
# it. The program could then retrieve only products related to the customer's tags
# instead of checking every product. A database or search system with indexed tag
# fields could also handle filtering and sorting efficiently. The index would need to
# be updated when products or tags changed. For this small assignment, the current
# list and set approach is simpler and adequate, but indexing would help as the
# catalog and number of searches grow.

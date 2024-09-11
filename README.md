# flask_devops

I've setup a dummy flask project with tests and a simple workflow with ci.yml to explore github actions

# tests

the Tests:

    test_get_items: Tests that the /items endpoint returns the list of items with a status code of 200.
    test_get_item: Tests that the /items/<id> endpoint returns a specific item by its ID.
    test_get_item_not_found: Tests that the API returns a 404 status code when an item is not found.
    test_create_item: Tests that a new item can be created using the /items POST endpoint.

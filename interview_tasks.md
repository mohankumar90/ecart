Tasks:

1. Write a view function with POST method, that takes a parameters the follwoing: ```user_id``` and a ```date```.
And it should return similar to the following:

    ```
    {
        "total_orders": 3,
        "total_amount_spent": 120.50,
        "most_frequent_item": "USB Cable"
    }
    ```

2. Write a function, it takes a string. Evaluate the given string for password validation requirements as follows, and return True if all validations are passes, otherwise False:
    - Min 8 characters and max 16 characters
    - Atleast 1 capital and 1 small leters should be there
    - Atleast 1 numeric should be there
    - Atleast 1 special character, and the allowed special characters are:   ! @ # * &
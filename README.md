# UnitCirclePracticer

- Class to help create quizzes for mental unit circle conversion
- Helps practice the following
    - Radians to degrees
    - Degrees to radians
    - Find coordinates from radians
    - Find coordinates from degrees
- It simply prints out the generated results
- To generate quiz
    - Import the unitCircle class
    ```py
    from unitCircle import unitCircle
    ```
    - Initialize the circle
    ```py
    circle = unitCircle()
    ```
    - Types of quizzes that can be generated, `degtorad`: degrees to radians/radians to degrees, and `degradtocoor`: degrees/radians to coordinate point
    ```py
    print(circle.generateQuiz(10, "degtorad")[0])
    print()
    print(circle.generateQuiz(10, "degradtocoor")[0])
    ```
    - Answer keys can also be generated for quizzes
    ```py
    quiz = circle.generateQuiz(10, "degradtocoor")
    print(quiz[0]) # quiz
    print()
    print(quiz[1]) # key
    ```
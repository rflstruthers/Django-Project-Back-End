# Live Project

## Introduction
For the last two weeks of my time at the tech academy, I worked with my peers in a team developing a full scale Django Web Application in Python. Working on a legacy codebase was a great learning oppertunity for fixing bugs, cleaning up code, and adding requested features. I saw how a good developer works with what they have to make a quality product. I worked on several [back end stories](#back-end-stories) that I am very proud of and was abale to gain experience both adding a new feature for the application and updating existing code. Over the two week sprint I also had the opportunity to work on some other project management and team programming [skills](#other-skills-learned) that have made me a better developer.

Below are descriptions of the stories I worked on, along with code snippets and navigation links. Some of the full code files I worked on are in this repo.

## Back End Stories
[Menu Application Addition](#menu-application-addition)
[Cafe Review](#cafe-review)
[Suntracker API Upgrade](#suntracker-api-upgrade)

### Menu Application Addition
The project had an existing restaurant menu application that allowed for the creation of new menu items. The story was to create a way to obtain and display recipe inspiration for new menu items. I wanted to allow the user to search for recipes based on ingredient, so I found an appropriate API that would return the data required by the story and used the users input as a parameter in the API.

    def inspiration(request):
        #If user typed in an ingredient:
        if request.method == 'POST':
            try:
                #meal finder API, search by main ingredient
                food_url = 'https://api.edamam.com/search?q={}&app_id=$82718192&app_key=$c59f26352fa32471be36ddc4602e1f56&from=0&to=3'

                #gets user input for main ingredient from menu_inspiration.html
                ingredient = request.POST.get('ingredient_name', None)

                #Combines the url with the user input:
                end_point_url = food_url.format(ingredient)

                #Sends that url to meal API and stores the JSON file it gets back in 'food_data_json' variable
                food_data_json = requests.get(end_point_url).text
                
I took the JSON response and converted it to a dictionary data type, and from that constructed a new dictionary populated with the relevant data. I did the same for an API that responded with a random drink recipe. 

                # json.loads reads and converts JSON from "food_data_json" to Dictionary data type and stores it in 'food_data' variable
                food_data = json.loads(food_data_json)

                #Constructing a Dictionary that will contain all the information needed from the meal JSON response
                meals = {
                    'ingredient' : food_data['q'],
                    'recipe_1' : food_data['hits'][0]['recipe']['label'],
                    'image_1' : food_data['hits'][0]['recipe']['image'],
                    'link_1' : food_data['hits'][0]['recipe']['url'],
                    'recipe_2' : food_data['hits'][1]['recipe']['label'],
                    'image_2' : food_data['hits'][1]['recipe']['image'],
                    'link_2' : food_data['hits'][1]['recipe']['url'],
                    'recipe_3' : food_data['hits'][2]['recipe']['label'],
                    'image_3' : food_data['hits'][2]['recipe']['image'],
                    'link_3' : food_data['hits'][2]['recipe']['url'],
                }

                # API for random drink
                drink_url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
                drink_data_json = requests.get(drink_url).text
                drink_data = json.loads(drink_data_json)
                print("\DRINK JSON: \n>>>{}{}".format(drink_data, '<<<'))

                drink = {
                    'name' : drink_data['drinks'][0]['strDrink'],
                    'image' : drink_data['drinks'][0]['strDrinkThumb'],
                    'instructions' : drink_data['drinks'][0]['strInstructions'],
                    'ingredient_1' : drink_data['drinks'][0]['strIngredient1'],
                    'ingredient_2' : drink_data['drinks'][0]['strIngredient2'],
                    'ingredient_3' : drink_data['drinks'][0]['strIngredient3'],
                    'ingredient_4' : drink_data['drinks'][0]['strIngredient4'],
                    'ingredient_5' : drink_data['drinks'][0]['strIngredient5'],
                    'ingredient_6' : drink_data['drinks'][0]['strIngredient6'],
                    'ingredient_7' : drink_data['drinks'][0]['strIngredient7'],
                    'ingredient_8' : drink_data['drinks'][0]['strIngredient8'],
                    'ingredient_9' : drink_data['drinks'][0]['strIngredient9'],
                    'ingredient_10' : drink_data['drinks'][0]['strIngredient10'],
                    'amount_1' : drink_data['drinks'][0]['strMeasure1'],
                    'amount_2' : drink_data['drinks'][0]['strMeasure2'],
                    'amount_3' : drink_data['drinks'][0]['strMeasure3'],
                    'amount_4' : drink_data['drinks'][0]['strMeasure4'],
                    'amount_5' : drink_data['drinks'][0]['strMeasure5'],
                    'amount_6' : drink_data['drinks'][0]['strMeasure6'],
                    'amount_7' : drink_data['drinks'][0]['strMeasure7'],
                    'amount_8' : drink_data['drinks'][0]['strMeasure8'],
                    'amount_9' : drink_data['drinks'][0]['strMeasure9'],
                    'amount_10' : drink_data['drinks'][0]['strMeasure10'],   
                }

                return render(request, 'menu/menu_inspiration_search.html', {'meals' : meals, 'drink' : drink})
                
I handled errors in by redirecting the user to an error page if their search string was invalid.

            #If the user enters invalid search
            except:
                return render(request, 'menu/menu_inspiration_error.html')

        #When page is first loaded
        else:
            return render(request, 'menu/menu_inspiration.html')
            
The drink data contained up to 10 ingredients, however not all the recipes had 10 ingredients. In the template, I wanted to display the list of ingredients and their ammounts, but only for the ingredients that existed in the recipe. I accomplished this by creating an IF statement for each ingredient to determine if it existed, and displaying it in the list if it did.

    <ul>
      <li>{{ drink.amount_1 }} {{ drink.ingredient_1 }}</li>
      <li>{{ drink.amount_2 }} {{ drink.ingredient_2 }}</li>
      {% if  drink.ingredient_3 %}
      <li>{{ drink.amount_3 }} {{ drink.ingredient_3 }}</li>
      {% endif %}
      {% if  drink.ingredient_4 %}
      <li>{{ drink.amount_4 }} {{ drink.ingredient_4 }}</li>
      {% endif %}
      {% if  drink.ingredient_5 %}
      <li>{{ drink.amount_4 }} {{ drink.ingredient_5 }}</li>
      {% endif %}
      {% if  drink.ingredient_6 %}
      <li>{{ drink.amount_6 }} {{ drink.ingredient_6 }}</li>
      {% endif %}
      {% if  drink.ingredient_7 %}
      <li>{{ drink.amount_7 }} {{ drink.ingredient_7 }}</li>
      {% endif %}
      {% if  drink.ingredient_8 %}
      <li>{{ drink.amount_8 }} {{ drink.ingredient_8 }}</li>
      {% endif %}
      {% if  drink.ingredient_9 %}
      <li>{{ drink.amount_9 }} {{ drink.ingredient_9 }}</li>
      {% endif %}
      {% if  drink.ingredient_10 %}
      <li>{{ drink.amount_10 }} {{ drink.ingredient_10 }}</li>
      {% endif %}
    </ul>
    
This story gave me experience researching to find the correct API for the task given to me as well as using user input as part of the API to influence the response data. Tackling the ingredient display problem gave me practice using Django Template Language to perform logic in the template.

### Cafe Review



### Suntracker API Upgrade



## Other Skills Learned
* Working with a group of developers to identify bugs to the improve usability of an application.
* Improving project flow by communicating about who needs to check out which files for their current story.
* Learning new efficiencies from other developers by observing their workflow and asking questions.  
* Practice with team programming/pair programming when one developer runs into a bug they cannot solve.
* Participating in daily Stand-Up's to update the Project Manager and peers on my work.
* Planning how to complete a User Story and implementing that plan to satify the Story requirements.
* Producing results by a specified deadline.
  
*Jump to: [Back End Stories](#back-end-stories), [Page Top](#live-project)*

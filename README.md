# Live Project

## Introduction
During my internship at Prosper IT Consulting, I worked with my peers in a team developing a full scale Django Web Application in Python. During a two week sprint, I worked on the back end of the project. Working on a legacy codebase was a great learning oppertunity for fixing bugs, cleaning up code, and adding requested features. I saw how a good developer works with what they have to make a quality product. I worked on several [back end stories](#back-end-stories) that I am very proud of and was abale to gain experience both adding a new feature for the application and updating existing code. Over the two week sprint I also had the opportunity to work on some other project management and team programming [skills](#other-skills-learned) that have made me a better developer.

Below are descriptions of the stories I worked on, along with code snippets and navigation links. Some of the full code files I worked on are in this repo.

## Back End Stories
[Menu Application Addition](#menu-application-addition) | 
[Cafe Review](#cafe-review) | 
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
The project had a cafe application and I was tasked with allowing the user to create a new review of the cafe and display any previous reviews. I used Django Form and Model classes to accomplish the story objectives. I first created a Model class for a review along with relevant fields.

    class Review(models.Model):
        RATING_CHOICES = {
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        }
        date_visited = models.DateField(null=True)
        date = models.DateTimeField(auto_now_add=True)
        name = models.CharField(max_length=100)
        comment = models.TextField(max_length=1000)
        rating = models.IntegerField(choices=RATING_CHOICES)
        objects = models.Manager()

I then created a ModelForm class to allow the user to write a review and update the Review table in the database. I included the fields from the Model that I wanted the user to be able to edit. 

    class ReviewForm(ModelForm):

        class Meta:
            model = Review
            fields = ('name', 'date_visited', 'comment', 'rating')

I wrote a method for creating a review and as well as one for displaying any previous reviews.

    def review(request):
    context = {'reviews': Review.objects}
    return render(request, 'cafe/review.html', context)

    def leave_review(request):
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.save()
                return HttpResponseRedirect('/cafe/review/')
        else:
            form = ReviewForm()
        return render(request, 'cafe/leave_review.html', {'form': form})
        
I formatted the review.html and leave_review.html pages to enable the user to easily fill out the review form as well as view previous reviews. 

I gained knowledge and practice utilizing a database in a Django application. I was able to sucessfully create a Model class with appropriate attributes and then use a ModelForm based off that Model to update the database. The skills I developed while completing this story gave me a better understanding of how a Django web application interacts with a database. 

### Suntracker API Upgrade
The project had an existing application that used an API obtain sunrise and sunset times for the users location based on their IP address. The story asked to replace the existing API with a new one that would obtain moon data along with sun data. I researched the API documentation and determined the parameters needed were latitude, longitude, date, and timezone. There was an existing method for obtaining the users latitude, longitude, and timezone. However, the timezone format that the method returned was a string name of the timezone, while the API required the timezone parameter to be the UTC offset integer for the timezone. I used the pytz module to correctly format the timezone for the API. I used the data in the JSON API response to create a dictionary containing the data I wanted to display to the user. The times needed formatting from 24 hour time to 12 hour time, so I created a for loop to format each time in the dictionary correctly.

    def suntracker(location):
        #API:
        url = 'https://api.solunar.org/solunar/{},{},{},{}'
        # Format date for API and get latitude and longitude data from User_LatLon() method
        suntracker_date = datetime.today().strftime('%Y%m%d')
        Latitude, Longitude, timezone  = User_LatLon()
        # Get timezone and format it appropriately for API
        suntracker_tz = datetime.now(pytz.timezone(timezone)).strftime('%z')
        suntracker_tz = int(str(suntracker_tz)[:-2])
        # Format API with variables and converts returned Json data to dictionary
        end_point_url = url.format(Latitude, Longitude, suntracker_date, suntracker_tz)
        sun_data_json = requests.get(end_point_url).text
        sun_data = json.loads(sun_data_json)
        #Construct a new dictionary of needed data
        solunar_data = {
                'sunrise' : sun_data['sunRise'],
                'sunset' : sun_data['sunSet'],
                'moonrise' : sun_data['moonRise'],
                'moonset' : sun_data['moonSet'],
                'moonphase' : sun_data['moonPhase'],
            }
        # Format the displayed times for sunrise, sunset, moonrise, and moonset
        counter = 0
        for key in solunar_data:
            solunar_data[key] = ((datetime.strptime(solunar_data[key], "%H:%M")).strftime("%I:%M %p")).strip("0")
            counter += 1
            if counter == 4:
                break

        context = {'Location': location, 'solunar_data': solunar_data }
        return context

This story gave me good experience looking over existing code to determine how it was functioning, and then making the changes required to fulful the story requirements. I was able to make updates to existing code without breaking other parts of the application.


## Other Skills Learned
* Working with a group of developers to identify bugs to the improve usability of an application.
* Improving project flow by communicating about who needs to check out which files for their current story.
* Learning new efficiencies from other developers by observing their workflow and asking questions.  
* Practice with team programming/pair programming when one developer runs into a bug they cannot solve.
* Participating in daily Stand-Up's to update the Project Manager and peers on my work.
* Planning how to complete a User Story and implementing that plan to satify the Story requirements.
* Producing results by a specified deadline.
  
*Jump to: [Back End Stories](#back-end-stories), [Page Top](#live-project)*

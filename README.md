The application performs following steps:

1. User visits the URL (In our case it will be the local url) - Log in is not required. All requets are anonymous.
2. The home page renders. It will only have a search box where you can search for one single term. (ex. food, shooting, social)
3. Once the searh button is hit, the first 10 results will be shown in the search page:
4. If the term is searched for the first time, we get results from play.google.com/store - parse page & extract App ID, app name, developer name, developer email, icon url and store each field into the database through Django Models
5. If the term is alredy searched one - then just displays the cached results from database
6. When 1 of the 10 displayed search result is clicked - it opens a details page with some of the deatils the we were able to extract from the Play Store.
7. There is a "back" button in your details page to take you back to the "search results" page that you came from


The application uses default port 8000.

'pip install -r requirements.txt' before running the app
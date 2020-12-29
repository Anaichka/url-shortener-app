# url-shortener-app

<h2><b>How to use:</b></h2>
 
 Run Flask app. Then send POST request to "/shorten" route with body which includes dict: 
 - `{"url": url_to_short, "expiredDate": number_of_days}`
 
 If request was sent right, you'll get a json-dict as answer with format: 
 - `{"success": true, "hash": your_hash, "url": "your_new_short_url"}`
 
 Expired dates avaible: 1 day, 3 days, 7 days, 30 days, 90 days and 365 days.

Also it is avaible to run app and use service manually. While app is running there is a webpage, where you can paste your long link and choose expired date from dropdown menu. After clicking <b>"submit"</b> button short link will appear below input field.

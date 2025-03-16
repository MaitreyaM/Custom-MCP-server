Brave Web Search API
Introduction
Brave Web Search API is a REST API to query Brave Search and get back search results from the web. The following sections describe how to curate requests, including parameters and headers, to Brave Web Search API and get a JSON response back.

To try the API on a Free plan, you’ll still need to subscribe — you simply won’t be charged. Once subscribed, you can get an API key in the API Keys section.

Endpoints
Brave Search API exposes multiple endpoints for specific types of data, based on the level of your subscription. If you don’t see the endpoint you’re interested in, you may need to change your subscription.

https://api.search.brave.com/res/v1/web/search

Example
A request has to be made to the web search endpoint. An example CURL request is given below.



curl -s --compressed "https://api.search.brave.com/res/v1/web/search?q=brave+search" \
  -H "Accept: application/json" \
  -H "Accept-Encoding: gzip" \
  -H "X-Subscription-Token: <YOUR_API_KEY>"

The response specification for Web Search API can be seen in the WebSearchApiResponse model.

Next Steps
To learn what parameters are available and what responses can be expected while querying Brave Web Search API, please review the following pages:

Query Parameters
Request Headers
Response Headers
Response Objects
Brave Local Search API
Introduction
Brave Local Search API provides enrichments for location search results.

Access to Local API is available through the Pro plans.

Endpoints
Brave Local Search API is currently available at the following endpoints and exposes an API to get extra information about a location, including pictures and related web results.

https://api.search.brave.com/res/v1/local/pois

The endpoint supports batching and retrieval of extra information of up to 20 locations with a single request.

The local API also includes an endpoint to get an AI generated description for a location.

https://api.search.brave.com/res/v1/local/descriptions

Example
An initial request has to be made to web search endpoint with a given query. An example CURL request is given below.



curl -s --compressed "https://api.search.brave.com/res/v1/web/search?q=greek+restaurants+in+san+francisco" \
  -H "Accept: application/json" \
  -H "Accept-Encoding: gzip" \
  -H "X-Subscription-Token: <YOUR_API_KEY>"

If the query returns a list of locations, as in this case, each location result has an id field, which is a temporary ID that can be used to retrieve extra information about the location. An example from the locations result is given below.

{
  "locations": {
    "results": [
      {
        "id": "1520066f3f39496780c5931d9f7b26a6",
        "title": "Pangea Banquet Mediterranean Food"
      },
      {
        "id": "d00b153c719a427ea515f9eacf4853a2",
        "title": "Park Mediterranean Grill"
      },
      {
        "id": "4b943b378725432aa29f019def0f0154",
        "title": "The Halal Mediterranean Co."
      }
    ]
  }
}

The id value can be used to further fetch extra information about the location. An example request is given below.



curl -s --compressed "https://api.search.brave.com/res/v1/local/pois?ids=1520066f3f39496780c5931d9f7b26a6&ids=d00b153c719a427ea515f9eacf4853a2" \
  -H "accept: application/json" \
  -H "Accept-Encoding: gzip" \
  -H "x-subscription-token: <YOUR_API_KEY>"

An AI generated description associated with a location can be further fetched using the example below.



curl -s --compressed "https://api.search.brave.com/res/v1/local/descriptions?ids=1520066f3f39496780c5931d9f7b26a6&ids=d00b153c719a427ea515f9eacf4853a2" \
  -H "accept: application/json" \
  -H "Accept-Encoding: gzip" \
  -H "x-subscription-token: <YOUR_API_KEY>"

The response specification for Local Search API can be seen in the LocalPoiSearchApiResponse and LocalDescriptionsSearchApiResponse models.

Next Steps
To learn what parameters are available and what responses can be expected while querying Brave Web Search API, please review the following pages:

Query Parameters
Request Headers
Response Headers
Response Objects

Query Parameters
# Web Search API
This table lists the query parameters supported by the Web Search API. Some are required, but most are optional.

Parameter	Required	Type	Default	Description
q	true	string		
The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.

country	false	string	US	
The search query country, where the results come from.

The country string is limited to 2 character country codes of supported countries. For a list of supported values, see Country Codes.

search_lang	false	string	en	
The search language preference.

The 2 or more character language code for which the search results are provided. For a list of possible values, see Language Codes.

ui_lang	false	string	en-US	
User interface language preferred in response.

Usually of the format ‘<language_code>-<country_code>’. For more, see RFC 9110. For a list of supported values, see UI Language Codes.

count	false	number	20	
The number of search results returned in response.

The maximum is 20. The actual number delivered may be less than requested. Combine this parameter with offset to paginate search results.

offset	false	number	0	
The zero based offset that indicates number of search results per page (count) to skip before returning the result. The maximum is 9. The actual number delivered may be less than requested based on the query.

In order to paginate results use this parameter together with count. For example, if your user interface displays 20 search results per page, set count to 20 and offset to 0 to show the first page of results. To get subsequent pages, increment offset by 1 (e.g. 0, 1, 2). The results may overlap across multiple pages.

safesearch	false	string	moderate	
Filters search results for adult content.

The following values are supported:

off: No filtering is done.
moderate: Filters explicit content, like images and videos, but allows adult domains in the search results.
strict: Drops all adult content from search results.
freshness	false	string		
Filters search results by when they were discovered.

The following values are supported: - pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30.

text_decorations	false	bool	1	
Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters).

spellcheck	false	bool	1	
Whether to spellcheck provided query. If the spellchecker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model.

result_filter	false	string		
A comma delimited string of result types to include in the search response.

Not specifying this parameter will return back all result types in search response where data is available and a plan with the corresponding option is subscribed. The response always includes query and type to identify any query modifications and response type respectively.

Available result filter values are: - discussions - faq - infobox - news - query - summarizer - videos - web - locations

Example result filter param result_filter=discussions, videos returns only discussions, and videos responses. Another example where only location results are required, set the result_filter param to result_filter=locations.

goggles_id	false	string		
Goggles act as a custom re-ranking on top of Brave’s search index. For more details, refer to the Goggles repository. This parameter is deprecated. Please use the goggles parameter.

goggles	false	string		
Goggles act as a custom re-ranking on top of Brave’s search index. The parameter supports both a url where the Goggle is hosted or the definition of the goggle. For more details, refer to the Goggles repository.

units	false	string		
The measurement units. If not provided, units are derived from search country.

Possible values are: - metric: The standardized measurement system - imperial: The British Imperial system of units.

extra_snippets	false	bool		
A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts.

Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans.

summary	false	bool		
This parameter enables summary key generation in web search results. This is required for summarizer to be enabled.


You can also optimise your search query by using search operators.

# Local Search API
This table lists the query parameters supported by the Local Search API. Some are required, but most are optional.

Parameter	Required	Type	Default	Description
ids	true	list[string]		
Unique identifier for the location. Ids can not be empty. Maximum of 20 ids per request. The parameter can be repeated to query for multiple ids.

search_lang	false	string	en	
The search language preference.

The 2 or more character language code for which the search results are provided. For a list of possible values, see Language Codes.

ui_lang	false	string	en-US	
User interface language preferred in response.

Usually of the format ‘<language_code>-<country_code>’. For more, see RFC 9110. For a list of supported values, see UI Language Codes.

units	false	string		
The measurement units. If not provided, units are derived from search country.

Possible values are: - metric: The standardized measurement system - imperial: The British Imperial system of units.





Request Headers
# Web Search API Request Headers
This table lists the request headers supported by the Web Search API. Most are optional, but note that sending more information in headers (such as client location) will improve search results.

Header	Required	Name	Description
Accept	false	Accept	
The default supported media type is application/json

Accept-Encoding	false	Accept Encoding	
The supported compression type is gzip.

Api-Version	false	Web Search API Version	
The Brave Web Search API version to use. This is denoted by the format YYYY-MM-DD. The latest version is used by default, and the previous ones can be found in the API Changelog.

Cache-Control	false	Cache Control	
Search will return cached web search results by default. To prevent caching, set the Cache-Control header to no-cache. This is currently done as best effort.

User-Agent	false	User Agent	
The user agent of the client sending the request. Search can utilize the user agent to provide a different experience depending on the client sending the request.

The user agent should follow the commonly used browser agent strings on each platform. For more information on curating user agents, see RFC 9110.

User agent string examples by platform:

Android: Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36
iOS: Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1
macOS: Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
Windows: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
X-Loc-Lat	false	Latitude	
The latitude of the client’s geographical location in degrees, to provide relevant local results. The latitiude must be greater than or equal to -90.0 degrees and less than or equal to +90.0 degrees.

X-Loc-Long	false	Longitude	
The longitude of the client’s geographical location in degrees, to provide relevant local results. The longitude must be greater than or equal to -180.0 degrees and less than or equal to +180.0 degrees.

X-Loc-Timezone	false	Timezone	
The IANA timezone for the client’s device, for example America/New_York.

For complete list of IANA timezones and location mappings see IANA Database and Geonames Database.

X-Loc-City	false	City Name	
The generic name of the client city.

X-Loc-State	false	State Code	
The code representing the client’s state/region, can be up to 3 characters long.

The region is the first-level subdivision (the broadest or least specific) of the ISO 3166-2 code.

X-Loc-State-Name	false	State Name	
The name of the client’s state/region.

The region is the first-level subdivision (the broadest or least specific) of the ISO 3166-2 code.

X-Loc-Country	false	Country Code	
The two letter code for the client’s country.

For a list of country codes, see ISO 3166-1 alpha-2

X-Loc-Postal-Code	false	Postal Code	
The postal code of the client’s location.

X-Subscription-Token	true	Authentication token	
The secret token for the subscribed plan to authenticate the request. Can be obtained from API Keys.

# Local Search API Request Headers
This table lists the request headers supported by the Local Search API, most of which are optional.

Header	Required	Name	Description
Accept	false	Accept	
The default supported media type is application/json

Accept-Encoding	false	Accept Encoding	
The supported compression type is gzip.

Api-Version	false	Web Search API Version	
The Brave Web Search API version to use. This is denoted by the format YYYY-MM-DD. The latest version is used by default, and the previous ones can be found in the API Changelog.

Cache-Control	false	Cache Control	
Search will return cached web search results by default. To prevent caching, set the Cache-Control header to no-cache. This is currently done as best effort.

User-Agent	false	User Agent	
The user agent of the client sending the request. Search can utilize the user agent to provide a different experience depending on the client sending the request.

The user agent should follow the commonly used browser agent strings on each platform. For more information on curating user agents, see RFC 9110.

User agent string examples by platform:

Android: Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36
iOS: Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1
macOS: Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
Windows: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
X-Subscription-Token	true	Authentication token	
The secret token for the subscribed plan to authenticate the request. Can be obtained from API Keys.


Response Headers
Global
This table lists the response headers supported by the Web Search API.

Header	Name	Description
X-RateLimit-Limit	Rate Limit	
Rate limits associated with the requested plan.

An example rate limit X-RateLimit-Limit: 1, 15000 means 1 request per second and 15000 requests per month.

X-RateLimit-Policy	Rate Limit Policy	
Rate limit policies currently associated with the requested plan.

An example policy X-RateLimit-Policy: 1;w=1, 15000;w=2592000 means a limit of 1 request over a 1 second window and 15000 requests over a month window. The windows are always given in seconds.

X-RateLimit-Remaining	Rate Limit Remaining	
Remaining quota units associated with the expiring limits.

An example remaining limit X-RateLimit-Remaining: 1, 1000 indicates the API is able to be accessed once during the current second, and 1000 times over the current month.

Note: Only successful requests are counted and billed.

X-RateLimit-Reset	Rate Limit Reset	
The number of seconds until the quota associated with the expiring limits resets.

An example reset limit X-RateLimit-Reset: 1, 1419704 means a single request can be done again in a second and in 1419704 seconds the full monthly quota associated with the plan will be available again.



Response Objects
# WebSearchApiResponse
Top level response model for successful Web Search API requests. The response will include the relevant keys based on the plan subscribed, query relevance or applied result_filter as a query parameter. The API can also respond back with an error response based on invalid subscription keys and rate limit events.

Field	Type	Required	Description
type	"search"	true	
The type of web search API result. The value is always search.

discussions	Discussions	false	
Discussions clusters aggregated from forum posts that are relevant to the query.

faq	FAQ	false	
Frequently asked questions that are relevant to the search query.

infobox	GraphInfobox	false	
Aggregated information on an entity showable as an infobox.

locations	Locations	false	
Places of interest (POIs) relevant to location sensitive queries.

mixed	MixedResponse	false	
Preferred ranked order of search results.

news	News	false	
News results relevant to the query.

query	Query	false	
Search query string and its modifications that are used for search.

videos	Videos	false	
Videos relevant to the query.

web	Search	false	
Web search results relevant to the query.

summarizer	Summarizer	false	
Summary key to get summary results for the query.

rich	RichCallbackInfo	false	
Callback information for rich results.

# LocalPoiSearchApiResponse
Top level response model for successful Local Search API request to get extra information for locations. The response will include a list of location results corresponding to the ids in the request. The API can also respond back with an error response in cases like too many ids being requested, invalid subscription keys, and rate limit events. Access to Local Search API requires a subscription to a Pro plan.

Field	Type	Required	Description
type	"local_pois"	true	
The type of local POI search API result. The value is always local_pois.

results	list [ LocationResult ]	false	
Location results matching the ids in the request.

# LocalDescriptionsSearchApiResponse
Top level response model for successful Local Search API request to get AI generated description for locations. The response includes a list of generated descriptions corresponding to the ids in the request. The API can also respond back with an error response in cases like too many ids being requested, invalid subscription keys, and rate limit events. Access to Local Search API requires a subscription to a Pro plan.

Field	Type	Required	Description
type	"local_descriptions"	true	
The type of local description search API result. The value is always local_descriptions.

results	list [ LocationDescription ]	false	
Location descriptions matching the ids in the request.

# Query
A model representing information gathered around the requested query.

Field	Type	Required	Description
original	string	true	
The original query that was requested.

show_strict_warning	bool	false	
Whether there is more content available for query, but the response was restricted due to safesearch.

altered	string	false	
The altered query for which the search was performed.

safesearch	bool	false	
Whether safesearch was enabled.

is_navigational	bool	false	
Whether the query is a navigational query to a domain.

is_geolocal	bool	false	
Whether the query has location relevance.

local_decision	string	false	
Whether the query was decided to be location sensitive.

local_locations_idx	int	false	
The index of the location.

is_trending	bool	false	
Whether the query is trending.

is_news_breaking	bool	false	
Whether the query has news breaking articles relevant to it.

ask_for_location	bool	false	
Whether the query requires location information for better results.

language	Language	false	
The language information gathered from the query.

spellcheck_off	bool	false	
Whether the spellchecker was off.

country	string	false	
The country that was used.

bad_results	bool	false	
Whether there are bad results for the query.

should_fallback	bool	false	
Whether the query should use a fallback.

lat	string	false	
The gathered location latitutde associated with the query.

long	string	false	
The gathered location longitude associated with the query.

postal_code	string	false	
The gathered postal code associated with the query.

city	string	false	
The gathered city associated with the query.

state	string	false	
The gathered state associated with the query.

header_country	string	false	
The country for the request origination.

more_results_available	bool	false	
Whether more results are available for the given query.

custom_location_label	string	false	
Any custom location labels attached to the query.

reddit_cluster	string	false	
Any reddit cluster associated with the query.

# Discussions
A model representing a discussion cluster relevant to the query.

Field	Type	Required	Description
type	"search"	true	
The type identifying a discussion cluster. Currently the value is always search.

results	list [ DiscussionResult ]	true	
A list of discussion results.

mutated_by_goggles	bool	true	
Whether the discussion results are changed by a Goggle. False by default.

# DiscussionResult (SearchResult)
A discussion result. These are forum posts and discussions that are relevant to the search query.

Field	Type	Required	Description
type	"discussion"	true	
The discussion result type identifier. The value is always discussion.

data	ForumData	false	
The enriched aggregated data for the relevant forum post.

# ForumData
Defines a result from a discussion forum.

Field	Type	Required	Description
forum_name	string	true	
The name of the forum.

num_answers	int	false	
The number of answers to the post.

score	string	false	
The score of the post on the forum.

title	string	false	
The title of the post on the forum.

question	string	false	
The question asked in the forum post.

top_comment	string	false	
The top-rated comment under the forum post.

# FAQ
Frequently asked questions relevant to the search query term.

Field	Type	Required	Description
type	"faq"	true	
The FAQ result type identifier. The value is always faq.

results	list [ QA ]	true	
A list of aggregated question answer results relevant to the query.

# QA
A question answer result.

Field	Type	Required	Description
question	string	true	
The question being asked.

answer	string	true	
The answer to the question.

title	string	true	
The title of the post.

url	string	true	
The url pointing to the post.

meta_url	MetaUrl	false	
Aggregated information about the url.

# MetaUrl
Aggregated information about a url.

Field	Type	Required	Description
scheme	string	true	
The protocol scheme extracted from the url.

netloc	string	true	
The network location part extracted from the url.

hostname	string	false	
The lowercased domain name extracted from the url.

favicon	string	true	
The favicon used for the url.

path	string	true	
The hierarchical path of the url useful as a display string.

# Search
A model representing a collection of web search results.

Field	Type	Required	Description
type	"search"	true	
A type identifying web search results. The value is always search.

results	list [ SearchResult ]	true	
A list of search results.

family_friendly	bool	true	
Whether the results are family friendly.

# SearchResult (Result)
Aggregated information on a web search result, relevant to the query.

Field	Type	Required	Description
type	"search_result"	true	
A type identifying a web search result. The value is always search_result.

subtype	"generic"	true	
A sub type identifying the web search result type.

is_live	bool	true	
Whether the web search result is currently live. Default value is False.

deep_results	DeepResult	false	
Gathered information on a web search result.

schemas	list [ list ]	false	
A list of schemas (structured data) extracted from the page. The schemas try to follow schema.org and will return anything we can extract from the HTML that can fit into these models.

meta_url	MetaUrl	false	
Aggregated information on the url associated with the web search result.

thumbnail	Thumbnail	false	
The thumbnail of the web search result.

age	string	false	
A string representing the age of the web search result.

language	string	true	
The main language on the web search result.

location	LocationResult	false	
The location details if the query relates to a restaurant.

video	VideoData	false	
The video associated with the web search result.

movie	MovieData	false	
The movie associated with the web search result.

faq	FAQ	false	
Any frequently asked questions associated with the web search result.

qa	QAPage	false	
Any question answer information associated with the web search result page.

book	Book	false	
Any book information associated with the web search result page.

rating	Rating	false	
Rating found for the web search result page.

article	Article	false	
An article found for the web search result page.

product	ProductReview	false	
The main product and a review that is found on the web search result page.

product_cluster	list [ ProductReview ]	false	
A list of products and reviews that are found on the web search result page.

cluster_type	string	false	
A type representing a cluster. The value can be product_cluster.

cluster	list [ Result ]	false	
A list of web search results.

creative_work	CreativeWork	false	
Aggregated information on the creative work found on the web search result.

music_recording	MusicRecording	false	
Aggregated information on music recording found on the web search result.

review	Review	false	
Aggregated information on the review found on the web search result.

software	Software	false	
Aggregated information on a software product found on the web search result page.

recipe	Recipe	false	
Aggregated information on a recipe found on the web search result page.

organization	Organization	false	
Aggregated information on a organization found on the web search result page.

content_type	string	false	
The content type associated with the search result page.

extra_snippets	list [ string ]	false	
A list of extra alternate snippets for the web search result.

# Result
A model representing a web search result.

Field	Type	Required	Description
title	string	true	
The title of the web page.

url	string	true	
The url where the page is served.

is_source_local	bool	true	
is_source_both	bool	true	
description	string	false	
A description for the web page.

page_age	string	false	
A date representing the age of the web page.

page_fetched	string	false	
A date representing when the web page was last fetched.

profile	Profile	false	
A profile associated with the web page.

language	string	false	
A language classification for the web page.

family_friendly	bool	true	
Whether the web page is family friendly.

# AbstractGraphInfobox (Result)
Shared aggregated information on an entity from a knowledge graph.

Field	Type	Required	Description
type	"infobox"	true	
The infobox result type identifier. The value is always infobox.

position	int	true	
The position on a search result page.

label	string	false	
Any label associated with the entity.

category	string	false	
Category classification for the entity.

long_desc	string	false	
A longer description for the entity.

thumbnail	Thumbnail	false	
The thumbnail associated with the entity.

attributes	list [ list [ string ] ]	false	
A list of attributes about the entity.

profiles	list [ Profile ] | list [ DataProvider ]	false	
The profiles associated with the entity.

website_url	string	false	
The official website pertaining to the entity.

ratings	list [ Rating ]	false	
Any ratings given to the entity.

providers	list [ DataProvider ]	false	
A list of data sources for the entity.

distance	Unit	false	
A unit representing quantity relevant to the entity.

images	list [ Thumbnail ]	false	
A list of images relevant to the entity.

movie	MovieData	false	
Any movie data relevant to the entity. Appears only when the result is a movie.

# GenericInfobox (AbstractGraphInfobox)
Aggregated information on a generic entity from a knowledge graph.

Field	Type	Required	Description
subtype	"generic"	true	
The infobox subtype identifier. The value is always generic.

found_in_urls	list [ string ]	false	
List of urls where the entity was found.

# EntityInfobox (AbstractGraphInfobox)
Aggregated information on an entity from a knowledge graph.

Field	Type	Required	Description
subtype	"entity"	true	
The infobox subtype identifier. The value is always entity.

# QAInfobox (AbstractGraphInfobox)
A question answer infobox.

Field	Type	Required	Description
subtype	"code"	true	
The infobox subtype identifier. The value is always code.

data	QAPage	true	
The question and relevant answer.

meta_url	MetaUrl	false	
Detailed information on the page containing the question and relevant answer.

# InfoboxWithLocation (AbstractGraphInfobox)
An infobox with location.

Field	Type	Required	Description
subtype	"location"	true	
The infobox subtype identifier. The value is always location.

is_location	bool	true	
Whether the entity a location.

coordinates	list [ float ]	false	
The coordinates of the location.

zoom_level	int	true	
The map zoom level.

location	LocationResult	false	
The location result.

# InfoboxPlace (AbstractGraphInfobox)
An infobox for a place, such as a business.

Field	Type	Required	Description
subtype	"place"	true	
The infobox subtype identifier. The value is always place.

location	LocationResult	true	
The location result.

# GraphInfobox
Aggregated information on an entity shown as an infobox.

Field	Type	Required	Description
type	"graph"	true	
The type identifier for infoboxes. The value is always graph.

results	GenericInfoboxQAInfoboxInfoboxPlaceInfoboxWithLocationEntityInfobox	true	
A list of infoboxes associated with the query.

# QAPage
Aggreated result from a question answer page.

Field	Type	Required	Description
question	string	true	
The question that is being asked.

answer	Answer	true	
An answer to the question.

# Answer
A response representing an answer to a question on a forum.

Field	Type	Required	Description
text	string	true	
The main content of the answer.

author	string	false	
The name of the author of the answer.

upvoteCount	int	false	
Number of upvotes on the answer.

downvoteCount	int	false	
The number of downvotes on the answer.

# Thumbnail
Aggregated details representing a picture thumbnail.

Field	Type	Required	Description
src	string	true	
The served url of the picture thumbnail.

original	string	false	
The original url of the image.

# LocationWebResult (Result)
A model representing a web result related to a location.

Field	Type	Required	Description
meta_url	MetaUrl	true	
Aggregated information about the url.

# LocationResult (Result)
A result that is location relevant.

Field	Type	Required	Description
type	"location_result"	true	
Location result type identifier. The value is always location_result.

id	string	false	
A Temporary id associated with this result, which can be used to retrieve extra information about the location. It remains valid for 8 hours…

provider_url	string	true	
The complete url of the provider.

coordinates	list [ float ]	false	
A list of coordinates associated with the location. This is a lat long represented as a floating point.

zoom_level	int	true	
The zoom level on the map.

thumbnail	Thumbnail	false	
The thumbnail associated with the location.

postal_address	PostalAddress	false	
The postal address associated with the location.

opening_hours	OpeningHours	false	
The opening hours, if it is a business, associated with the location .

contact	Contact	false	
The contact of the business associated with the location.

price_range	string	false	
A display string used to show the price classification for the business.

rating	Rating	false	
The ratings of the business.

distance	Unit	false	
The distance of the location from the client.

profiles	list [ DataProvider ]	false	
Profiles associated with the business.

reviews	Reviews	false	
Aggregated reviews from various sources relevant to the business.

pictures	PictureResults	false	
A bunch of pictures associated with the business.

action	Action	false	
An action to be taken.

serves_cuisine	list [ string ]	false	
A list of cuisine categories served.

categories	list [ string ]	false	
A list of categories.

icon_category	string	false	
An icon category.

results	LocationWebResult	false	
Web results related to this location.

timezone	string	false	
IANA timezone identifier.

timezone_offset	string	false	
The utc offset of the timezone.

# LocationDescription
AI generated description of a location result.

Field	Type	Required	Description
type	"local_description"	true	
The type of a location description. The value is always local_description.

id	string	true	
A Temporary id of the location with this description.

description	string	false	
AI generated description of the location with the given id.

# Locations
A model representing location results.

Field	Type	Required	Description
type	"locations"	true	
Location type identifier. The value is always locations.

results	list [ LocationResult ]	true	
An aggregated list of location sensitive results.

# MixedResponse
The ranking order of results on a search result page.

Field	Type	Required	Description
type	"mixed"	true	
The type representing the model mixed. The value is always mixed.

main	list [ ResultReference ]	false	
The ranking order for the main section of the search result page.

top	list [ ResultReference ]	false	
The ranking order for the top section of the search result page.

side	list [ ResultReference ]	false	
The ranking order for the side section of the search result page.

# ResultReference
The ranking order of results on a search result page.

Field	Type	Required	Description
type	string	true	
The type of the result.

index	int	false	
The 0th based index where the result should be placed.

all	bool	true	
Whether to put all the results from the type at specific position.

# Videos
A model representing video results.

Field	Type	Required	Description
type	videos	true	
The type representing the videos. The value is always videos.

results	list [ VideoResult ]	true	
A list of video results.

mutated_by_goggles	bool	false	
Whether the video results are changed by a Goggle. False by default.

# News
A model representing news results.

Field	Type	Required	Description
type	news	true	
The type representing the news. The value is always news.

results	list [ NewsResult ]	true	
A list of news results.

mutated_by_goggles	bool	false	
Whether the news results are changed by a Goggle. False by default.

# NewsResult (Result)
A model representing news results.

Field	Type	Required	Description
meta_url	MetaUrl	false	
The aggregated information on the url representing a news result

source	string	false	
The source of the news.

breaking	bool	true	
Whether the news result is currently a breaking news.

is_live	bool	true	
Whether the news result is currently live.

thumbnail	Thumbnail	false	
The thumbnail associated with the news result.

age	string	false	
A string representing the age of the news article.

extra_snippets	list [ string ]	false	
A list of extra alternate snippets for the news search result.

# PictureResults
A model representing a list of pictures.

Field	Type	Required	Description
viewMoreUrl	string	false	
A url to view more pictures.

results	list [ Thumbnail ]	true	
A list of thumbnail results.

# Action
A model representing an action to be taken.

Field	Type	Required	Description
type	string	true	
The type representing the action.

url	string	true	
A url representing the action to be taken.

# PostalAddress
A model representing a postal address of a location

Field	Type	Required	Description
type	"PostalAddress"	true	
The type identifying a postal address. The value is always PostalAddress.

country	string	false	
The country associated with the location.

postalCode	string	false	
The postal code associated with the location.

streetAddress	string	false	
The street address associated with the location.

addressRegion	string	false	
The region associated with the location. This is usually a state.

addressLocality	string	false	
The address locality or subregion associated with the location.

displayAddress	string	true	
The displayed address string.

# OpeningHours
Opening hours of a bussiness at a particular location.

Field	Type	Required	Description
current_day	list [ DayOpeningHours ]	false	
The current day opening hours. Can have two sets of opening hours.

days	list [ list [ DayOpeningHours ] ]	false	
The opening hours for the whole week.

# DayOpeningHours
A model representing the opening hours for a particular day for a business at a particular location.

Field	Type	Required	Description
abbr_name	string	true	
A short string representing the day of the week.

full_name	string	true	
A full string representing the day of the week.

opens	string	true	
A 24 hr clock time string for the opening time of the business on a particular day.

closes	string	true	
A 24 hr clock time string for the closing time of the business on a particular day.

# Contact
A model representing contact information for an entity.

Field	Type	Required	Description
email	string	false	
The email address.

telephone	string	false	
The telephone number.

# DataProvider
A model representing the data provider associated with the entity.

Field	Type	Required	Description
type	"external"	true	
The type representing the source of data. This is usually external.

name	string	true	
The name of the data provider. This can be a domain.

url	string	true	
The url where the information is coming from.

long_name	string	false	
The long name for the data provider.

img	string	false	
The served url for the image data.

# Profile
A profile of an entity.

Field	Type	Required	Description
name	string	true	
The name of the profile.

long_name	string	true	
The long name of the profile.

url	string	false	
The original url where the profile is available.

img	string	false	
The served image url representing the profile.

# Unit
A model representing a unit of measurement.

Field	Type	Required	Description
value	float	true	
The quantity of the unit.

units	string	true	
The name of the unit associated with the quantity.

# MovieData
Aggregated data for a movie result.

Field	Type	Required	Description
name	string	false	
Name of the movie.

description	string	false	
A short plot summary for the movie.

url	string	false	
A url serving a movie profile page.

thumbnail	Thumbnail	false	
A thumbnail for a movie poster.

release	string	false	
The release date for the movie.

directors	list [ Person ]	false	
A list of people responsible for directing the movie.

actors	list [ Person ]	false	
A list of actors in the movie.

rating	Rating	false	
Rating provided to the movie from various sources.

duration	string	false	
The runtime of the movie. The format is HH:MM:SS.

genre	list [ string ]	false	
List of genres in which the movie can be classified.

query	string	false	
The query that resulted in the movie result.

# Thing
A model describing a generic thing.

Field	Type	Required	Description
type	"thing"	true	
A type identifying a thing. The value is always thing.

name	string	true	
The name of the thing.

url	string	false	
A url for the thing.

thumbnail	Thumbnail	false	
Thumbnail associated with the thing.

# Person (Thing)
A model describing a person entity.

Field	Type	Required	Description
type	"person"	true	
A type identifying a person. The value is always person.

# Rating
The rating associated with an entity.

Field	Type	Required	Description
ratingValue	float	true	
The current value of the rating.

bestRating	float	true	
Best rating received.

reviewCount	int	false	
The number of reviews associated with the rating.

profile	Profile	false	
The profile associated with the rating.

is_tripadvisor	bool	true	
Whether the rating is coming from Tripadvisor.

# Book
A model representing a book result.

Field	Type	Required	Description
title	string	true	
The title of the book.

author	list [ Person ]	true	
The author of the book.

date	string	false	
The publishing date of the book.

price	Price	false	
The price of the book.

pages	int	false	
The number of pages in the book.

publisher	Person	false	
The publisher of the book.

rating	Rating	false	
A gathered rating from different sources associated with the book.

# Price
A model representing the price for an entity.

Field	Type	Required	Description
price	string	true	
The price value in a given currency.

price_currency	string	true	
The current of the price value.

# Article
A model representing an article.

Field	Type	Required	Description
author	list [ Person ]	false	
The author of the article.

date	string	false	
The date when the article was published.

publisher	Organization	false	
The name of the publisher for the article.

thumbnail	Thumbnail	false	
A thumbnail associated with the article.

isAccessibleForFree	bool	false	
Whether the article is free to read or is behind a paywall.

# ContactPoint (Thing)
A way to contact an entity.

Field	Type	Required	Description
type	"contact_point"	true	
A type string identifying a contact point. The value is always contact_point.

telephone	string	false	
The telephone number of the entity.

email	string	false	
The email address of the entity.

# Organization (Thing)
An entity responsible for another entity.

Field	Type	Required	Description
type	"organization"	true	
A type string identifying an organization. The value is always organization.

contact_points	list [ ContactPoint ]	false	
A list of contact points for the organization.

# HowTo
Aggregated information on a how to.

Field	Type	Required	Description
text	string	true	
The how to text.

name	string	false	
A name for the how to.

url	string	false	
A url associated with the how to.

image	list [ string ]	false	
A list of image urls associated with the how to.

# Recipe
Aggregated information on a recipe.

Field	Type	Required	Description
title	string	true	
The title of the recipe.

description	string	true	
The description of the recipe.

thumbnail	Thumbnail	true	
A thumbnail associated with the recipe.

url	string	true	
The url of the web page where the recipe was found.

domain	string	true	
The domain of the web page where the recipe was found.

favicon	string	true	
The url for the favicon of the web page where the recipe was found.

time	string	false	
The total time required to cook the recipe.

prep_time	string	false	
The preparation time for the recipe.

cook_time	string	false	
The cooking time for the recipe.

ingredients	string	false	
Ingredients required for the recipe.

instructions	list [ HowTo ]	false	
List of instructions for the recipe.

servings	int	false	
How many people the recipe serves.

calories	int	false	
Calorie count for the recipe.

rating	Rating	false	
Aggregated information on the ratings associated with the recipe.

recipeCategory	string	false	
The category of the recipe.

recipeCuisine	string	false	
The cuisine classification for the recipe.

video	VideoData	false	
Aggregated information on the cooking video associated with the recipe.

# Product
A model representing a product.

Field	Type	Required	Description
type	"Product"	true	
A string representing a product type. The value is always product.

name	string	true	
The name of the product.

category	string	false	
The category of the product.

price	string	true	
The price of the product.

thumbnail	Thumbnail	true	
A thumbnail associated with the product.

description	string	false	
The description of the product.

offers	list [ Offer ]	false	
A list of offers available on the product.

rating	Rating	false	
A rating associated with the product.

# Offer
An offer associated with a product.

Field	Type	Required	Description
url	string	true	
The url where the offer can be found.

priceCurrency	string	true	
The currency in which the offer is made.

price	string	true	
The price of the product currently on offer.

# Review
A model representing a review for an entity.

Field	Type	Required	Description
type	"review"	true	
A string representing review type. This is always review.

name	string	true	
The review title for the review.

thumbnail	Thumbnail	true	
The thumbnail associated with the reviewer.

description	string	true	
A description of the review (the text of the review itself).

rating	Rating	true	
The ratings associated with the review.

# Reviews
The reviews associated with an entity.

Field	Type	Required	Description
results	list [ TripAdvisorReview ]	true	
A list of trip advisor reviews for the entity.

viewMoreUrl	string	true	
A url to a web page where more information on the result can be seen.

reviews_in_foreign_language	bool	true	
Any reviews available in a foreign language.

# TripAdvisorReview
A model representing a Tripadvisor review.

Field	Type	Required	Description
title	string	true	
The title of the review.

description	string	true	
A description seen in the review.

date	string	true	
The date when the review was published.

rating	Rating	true	
A rating given by the reviewer.

author	Person	true	
The author of the review.

review_url	string	true	
A url link to the page where the review can be found.

language	string	true	
The language of the review.

# CreativeWork
A creative work relevant to the query. An example can be enriched metadata for an app.

Field	Type	Required	Description
name	string	true	
The name of the creative work.

thumbnail	Thumbnail	true	
A thumbnail associated with the creative work.

rating	Rating	false	
A rating that is given to the creative work.

# MusicRecording
Result classified as a music label or a song.

Field	Type	Required	Description
name	string	true	
The name of the song or album.

thumbnail	Thumbnail	false	
A thumbnail associated with the music.

rating	Rating	false	
The rating of the music.

# Software
A model representing a software entity.

Field	Type	Required	Description
name	string	false	
The name of the software product.

author	string	false	
The author of software product.

version	string	false	
The latest version of the software product.

codeRepository	string	false	
The code repository where the software product is currently available or maintained.

homepage	string	false	
The home page of the software product.

datePublisher	string	false	
The date when the software product was published.

is_npm	bool	false	
Whether the software product is available on npm.

is_pypi	bool	false	
Whether the software product is available on pypi.

stars	int	false	
The number of stars on the repository.

forks	int	false	
The numbers of forks of the repository.

ProgrammingLanguage	string	false	
The programming language spread on the software product.

# DeepResult
Aggregated deep results from news, social, videos and images.

Field	Type	Required	Description
news	list [ NewsResult ]	false	
A list of news results associated with the result.

buttons	list [ ButtonResult ]	false	
A list of buttoned results associated with the result.

videos	list [ VideoResult ]	false	
Videos associated with the result.

images	list [ Image ]	false	
Images associated with the result.

# VideoResult (Result)
A model representing a video result.

Field	Type	Required	Description
type	"video_result"	true	
The type identifying the video result. The value is always video_result.

video	VideoData	true	
Meta data for the video.

meta_url	MetaUrl	false	
Aggregated information on the URL

thumbnail	Thumbnail	false	
The thumbnail of the video.

age	string	false	
A string representing the age of the video.

# VideoData
A model representing metadata gathered for a video.

Field	Type	Required	Description
duration	string	false	
A time string representing the duration of the video. The format can be HH:MM:SS or MM:SS.

views	string	false	
The number of views of the video.

creator	string	false	
The creator of the video.

publisher	string	false	
The publisher of the video.

thumbnail	Thumbnail	false	
A thumbnail associated with the video.

tags	list [ string ]	false	
A list of tags associated with the video.

author	Profile	false	
Author of the video.

requires_subscription	bool	false	
Whether the video requires a subscription to watch.

# ButtonResult
A result which can be used as a button.

Field	Type	Required	Description
type	"button_result"	true	
A type identifying button result. The value is always button_result.

title	string	true	
The title of the result.

url	string	true	
The url for the button result.

# Image
A model describing an image

Field	Type	Required	Description
thumbnail	Thumbnail	true	
The thumbnail associated with the image.

url	string	false	
The url of the image.

properties	ImageProperties	false	
Metadata on the image.

# Language
A model representing a language.

Field	Type	Required	Description
main	string	true	
The main language seen in the string.

# ImageProperties
Metadata on an image.

Field	Type	Required	Description
url	string	true	
The original image URL.

resized	string	true	
The url for a better quality resized image.

placeholder	string	true	
The placeholder image url.

height	int	false	
The image height.

width	int	false	
The image width.

format	string	false	
The image format.

content_size	string	false	
The image size.

# Summarizer
Details on getting the summary.

Field	Type	Required	Description
type	"summarizer"	true	
The value is always summarizer.

key	string	true	
The key for the summarizer API.

# RichCallbackInfo
Callback information for rich results.

Field	Type	Required	Description
type	"rich"	true	
The value is always rich.

hint	RichCallbackHint	false	
The hint for the rich result.

# RichCallbackHint
The hint for the rich result.

Field	Type	Required	Description
vertical	string	true	
The name of the vertical of the rich result.

callback_key	string	true	
The callback key for the rich result.
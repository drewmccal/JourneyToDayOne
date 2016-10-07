# JourneyToDayOne
tinny python script I wrote to convert Journey backup to dayone compatible JSON while I was desperate (it's bare minimum and just converts what I personally needed at the point). Definitely not a *complete* conversion tool.
This script basically parses the multiple json files in a journey backup zip and converts it to DayOne format json file
There are no external requirements to run, just extract the Journey backup, place the py file inside the folder as the json files and run. A new file "Journal.json" is created. Just put this file in a zip and import with DayOne.
###NOTE:
 - this only imports the text, entry creation date/time and tags.
 I will try to update ( or perhaps someone else might beat me to it) so it can:
 - import photo(s) for entries
 - import other meta data that is common to both platforms -location, weather and activity.

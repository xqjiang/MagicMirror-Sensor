/* Magic Mirror Config Sample
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information how you can configurate this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */

var config = {
	address: "localhost", // Address to listen on, can be:
	                      // - "localhost", "127.0.0.1", "::1" to listen on loopback interface
	                      // - another specific IPv4/6 to listen on a specific interface
	                      // - "", "0.0.0.0", "::" to listen on any interface
	                      // Default, when address config is left out, is "localhost"
	port: 8080,
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], // Set [] to allow all IP addresses
	                                                       // or add a specific IPv4 of 192.168.1.5 :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
	                                                       // or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	language: "en",
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: "alert",
		},
		{
  			module: "MMM-GooglePhotos",
  			position: "middle_center",
  			config: {
    				albumId:"AAtMr7Lv78sQhFFHkm0wo3mGIK9xAsKMBgqT7PeGvf86uIZnzUKHxiXo2W3TwSbsR6FAjyk1e4Hf", // your album id(s) from result of `auth_and_test.js`
    				refreshInterval: 1000*60,  
    				scanInterval: 1000*60*10, // too many scans might cause API quota limit also.
    				//note(2018-07-29). It is some weird. API documents said temporal image url would live for 1 hour, but it might be broken shorter. So, per 10 min scanning could prevent dead url.

    				sort: "time", //'time', 'reverse', 'random'
    				showWidth: "1100px", // how large the photo will be shown as. (e.g;'100%' for fullscreen)
    				showHeight: "600px",
    				originalWidthPx: 1098, // original size of loaded image. (related with image quality)
    				originalHeightPx: 600, // Bigger size gives you better quality, but can give you network burden.
    				mode: "hybrid", // "cover" or "contain" (https://www.w3schools.com/cssref/css3_pr_background-size.asp)
    				//ADDED. "hybrid" : if you set as "hybrid" it will change "cover" and "contain" automatically by aspect ratio.
  			}
		},

		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "MMM-PIR-Sensor",
			config: {
				sensorPin: 26,
				powerSavingDelay:100
				}		
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "Upcoming Holidays",
			position: "top_left",
			config: {
				calendars: [
					{
						symbol: "calendar-check",
						url: "webcal://www.calendarlabs.com/ical-calendar/ics/67/Singapore_Holidays.ics"
					}
				]
			}
		},
		{
			module: "compliments",
			position: "bottom_center"
		},
		{
			module: "currentweather",
			position: "top_right",
			config: {
				location: "Singapore",
				locationID: "1880251",  //ID from http://bulk.openweathermap.org/sample/; unzip the gz file and find your city
				appid: "117ef4afecc553d3b18c1dd84308112d"
			}
		},
		{
			module: "weatherforecast",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				location: "Singapore",
				locationID: "1880251",  //ID from https://openweathermap.org/city
				appid: "117ef4afecc553d3b18c1dd84308112d"
			}
		},
		{
			module: "MMM-Stock",
			position: "middle_center",
			config: {
				companies: ["UNH", "TMO", "ILMN", "MDT", "A"]
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "New York Times",
						url: "http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"
					}
				],
				showSourceTitle: true,
				showPublishDate: true
			}
		},
	]

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}

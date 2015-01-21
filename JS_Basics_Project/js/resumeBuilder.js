var work = {
	"jobs": [
	{
		"employer": "Udacity",
		"title": "Programmer/ Code Reviewer",
		"location": "Dublin, Ireland",
		"dates": "January 2015 - Present",
		"url": "http://www.udacity.com",
		"description": "I work as a code reviewer for Udcaity, which involves grading and commenting on student projects for " +
		               "Udacity's Programming Foundations with Python course and also it's CS101 course. Grading is based on correctness," +
		               " comments in the code as well as style and design choices"
	},

	{
		"employer": "Mutual of America",
		"title": "Mutual Fund Accountant",
		"location": "New York",
		"dates": "June 2012 - August 2012",
		"url": "http://www.mutualofamerica.com/",
		"description": " I interned in the corporate finance department of Mutual of America in the summer of 2012." +
		" More specifically, I worked in the mutual fund pricing division as a junior fund accountant." +
		" Duties included the calculation of the Net Asset Value (NAV) of four funds, database administration and report preparation."
	}
	]
}

var projects = {
	"projects": [
	{
		"title": "TILBot",
		"start": "August 2014",
		"dates": "August 2014",
		"description": "This is a bot that crawls reddit's 'Today I Learned' (TIL) subreddit, checking for facts containing one or more keywords" +
		" entered by the user. If one was found, an email containing that fact and a URL containing its source is sent to the user.",
		"images": "images/reddit-alien.png",
		"url": "https://github.com/xkal36/Course_Projects/tree/master/Udacity_OOP_Project"
	}
	]
}

var bio = {
	"name": "Andrew Winterbotham",
	"role": "Programmer",
	"contacts": {
		"mobile": "+353 872121620",
		"email": "awinterbotham02@gmail.com",
		"github": "xkal36",
		"LinkedIn": "https://ie.linkedin.com/in/awinterbotham",
		"location": "Dublin, Ireland"
	},
	"welcomeMessage": "Hello and welcome to my online resume!",
	"skills": [
	"Python", "JavaScript", "HTML", "CSS", "Ruby", "C", "PHP"
	],
	"bioPic": "images/me.jpg"
}


var education = {
	"schools": [
	{
		"name": "Trinity College Dublin",
		"location": "Dublin",
		"degree": "BA",
		"majors": ["Economics"],
		"minor": "Business",
		"dates": 2015,
		"url": "http://www.tcd.ie"
	}
	]
	,
	"onlineCourses": [
		{
			"title": "JavaScript Syntax",
			"school": "Udacity",
			"dates": 2015,
			"url": "http://www.udacity.com/course/ud804"
		}
	]
}


// appends formatted school data to the web page
education.displaySchools = function() {
	for (school in education.schools) {
		$("#education").append(HTMLschoolStart);

		var formattedName = HTMLschoolName.replace("%data%", education.schools[school].name).replace("#", education.schools[school].url);
		var formattedDegree = HTMLschoolDegree.replace("%data%", education.schools[school].degree);
		var formattedDates = HTMLschoolDates.replace("%data%", education.schools[school].dates);
		var formattedLocation = HTMLschoolLocation.replace("%data%", education.schools[school].location);
		
		var schoolData = formattedName + formattedDegree + formattedDates + formattedLocation;

		$(".education-entry:last").append(schoolData);
		
		for (major in education.schools[school].majors) {
			var formattedMajor = HTMLschoolMajor.replace("%data%", education.schools[school].majors[major]);
			$(".education-entry:last").append(formattedMajor);
		}
	}
}


// appends formatted course data to the web page
education.displayCourses = function() {
	$("#education").append(HTMLonlineClasses);

	for (course in education.onlineCourses) {
		$("#education").append(HTMLschoolStart);

		var formattedTitle = HTMLonlineTitle.replace("%data%", education.onlineCourses[course].title).replace("#", education.onlineCourses[course].url);
		var formattedSchool = HTMLonlineSchool.replace("%data%", education.onlineCourses[course].school);
		var formattedDates = HTMLonlineDates.replace("%data%", education.onlineCourses[course].dates);
		var formattedURL = HTMLonlineURL.replace("%data%", education.onlineCourses[course].url).replace("#", education.onlineCourses[course].url);

		var onlineData = formattedTitle + formattedSchool + formattedDates + formattedURL;

		$(".education-entry:last").append(onlineData);
	}
}


// appends formatted skills data to the web page
bio.displaySkills = function() {
	if (bio.skills.length > 0) {
		$("#header").append(HTMLskillsStart);
	
		for (skill in bio.skills) {
			var formattedSkill = HTMLskills.replace("%data%", bio.skills[skill]);
		    $("#skills").append(formattedSkill);
		}
	}	
}


// creates and adds a bar chart representing level of 
// proficiency in each skill, using the chart.js library
bio.visualiseSkills = function() {
	var data = {
    	labels: bio.skills,
    	datasets: [
        	{
            label: "Skill Levels",
            fillColor: "rgba(151,187,205,0.5)",
            strokeColor: "rgba(151,187,205,0.8)",
            highlightFill: "rgba(151,187,205,0.75)",
            highlightStroke: "rgba(151,187,205,1)",
            data: [90, 80, 70, 70,65, 60, 50]
        	}
    	]
	};

	// Get context with jQuery - using jQuery's .get() method.
	var ctx = $("#myChart").get(0).getContext("2d");
	// This will get the first returned node in the jQuery collection.
	var myNewChart = new Chart(ctx);

	var myBarChart = new Chart(ctx).Bar(data);
}


// appends formatted work information to the resume
work.displayWork = function() {
	for (job in work.jobs) {
	$("#workExperience").append(HTMLworkStart);

	var formattedEmployer = HTMLworkEmployer.replace("%data%", work.jobs[job].employer).replace("#", work.jobs[job].url);
    var formattedTitle = HTMLworkTitle.replace("%data%", work.jobs[job].title);
	var formattedEmployerTitle = formattedEmployer + formattedTitle;
	
	var formattedDates = HTMLworkDates.replace("%data%", work.jobs[job].dates);
	var formattedLocation = HTMLworkLocation.replace("%data%", work.jobs[job].location);
	var formattedDescription = HTMLworkDescription.replace("%data%", work.jobs[job].description);
	
	$(".work-entry:last").append(formattedEmployerTitle);

	$(".work-entry:last").append(formattedDates);
	$(".work-entry:last").append(formattedLocation);
	$(".work-entry:last").append(formattedDescription);
	}	
}


// formats and puts the header html at the beginning of the page
bio.displayHeader = function() {
	var formattedName = HTMLheaderName.replace("%data%", bio.name);
	var formattedRole = HTMLheaderRole.replace("%data%", bio.role);

	$("#header").prepend(formattedRole);
	$("#header").prepend(formattedName);	
}


// formats and dispalys bio pic
bio.displayPic = function() {
	var formattedPic = HTMLbioPic.replace("%data%", bio.bioPic);
	$('#header').append(formattedPic);	
}


// formats and diaplays welcome message
bio.displayMessage = function() {
	var formattedMessage = HTMLWelcomeMsg.replace("%data%", bio.welcomeMessage);
	$('#header').append(formattedMessage);	
}


// formats and dispalys contact info to header and footer of the page
bio.displayContacts = function() {
	var formattedMobile = HTMLmobile.replace("%data%", bio.contacts.mobile);
	var formattedEmail = HTMLemail.replace("%data%", bio.contacts.email);
	var formattedLinkedIn = HTMLtwitter.replace("%data%", bio.contacts.LinkedIn);
	var formattedGithub = HTMLgithub.replace("%data%", bio.contacts.github);
	var formattedLocation = HTMLlocation.replace("%data%", bio.contacts.location);

	var formattedContacts = formattedMobile + formattedEmail + formattedLinkedIn + formattedGithub + formattedLocation;
    $("#topContacts").prepend(formattedContacts); 
    $("#footerContacts").append(formattedContacts); 
}	


// formats and appends project data to the page
projects.display = function() {
	for (project in projects.projects) {
		$("#projects").append(HTMLprojectStart);

		var formattedProjectTitle = HTMLprojectTitle.replace("%data%", projects.projects[project].title).replace("#", projects.projects[project].url);
		$(".project-entry:last").append(formattedProjectTitle);
		
		var formattedProjectDates = HTMLprojectDates.replace("%data%", projects.projects[project].dates);
		$(".project-entry:last").append(formattedProjectDates);
		
		var formattedProjectDesc = HTMLprojectDescription.replace("%data%", projects.projects[project].description);
		$(".project-entry:last").append(formattedProjectDesc);

		var formattedProjectImage = HTMLprojectImage.replace("%data%", projects.projects[project].images);	
		$(".project-entry:last").append(formattedProjectImage);
	}
}


// Records and outputs to the console the x and y coordinates of each mouse click
$(document).click(function(loc) {
	
	var x = loc.pageX;
	var y = loc.pageY;

	logClicks(x, y);
});


// Main funcntions: puts the page together in the correct order
bio.displayPic();
bio.displaySkills();
bio.displayHeader();
bio.displayContacts();

work.displayWork();

projects.display();

education.displaySchools();
education.displayCourses();

// Include google map with places worked
$("#mapDiv").append(googleMap);

// Create bar chart to visualise skills
bio.visualiseSkills();



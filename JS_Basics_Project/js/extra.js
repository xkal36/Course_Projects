//$("#main").append("Andrew Winterbotham");

var awesomeThoughts = "I am Andrew and I am AWESOME!";

console.log(awesomeThoughts);

var funThoughts = awesomeThoughts.replace("AWESOME", "FUN");

//$("#main").append(funThoughts);

var formattedName = HTMLheaderName.replace("%data%", "Andrew W.");

var role = "Engineer";

var formattedRole = HTMLheaderRole.replace("%data%", role);


$("#header").prepend(formattedRole);
$("#header").prepend(formattedName);

var education = {};

education["name"] = "Trinity College";
education["years"] = "2009-2014";
education["city"] = "Dublin";

$("#main").append(bio.name)
$("#main").append(work["position"]);
$("#main").append(education.name);

$("#main").append(internationalizeButton);

function inName(name) {
	name = name.trim().split(" ");
	console.log(name);
	name[1] = name[1].toUpperCase();
	name[0] = name[0].slice(0,1).toUpperCase() + name[0].slice(1).toLowerCase();

	return name[0] + " " + name[1];   
}



inName("Andy");









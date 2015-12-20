var data = {
	"band_id":23,
	"name":"Viki",
	"age":21,
	"telephone":"0887191474",
	"email":"viki_viki@ymail.com",
	"facebook":"Viki Viki"
};
$(document).ready(function(){
	$("#name").text(data["name"]);
	$("#id").text(data["band_id"]);
	$("#tel").text(data["telephone"]);
	$("#email").text(data["email"]);
	$("#fb").text(data["facebook"]);
})
var data = {
	"band_id":54,
	"name":"Stenly",
	"age":24,
	"telephone":"088134474",
	"email":"stenly@gmail.com",
	"facebook":"St Nik"
};
$(document).ready(function(){
	$("#friend_name").text(data["name"]);
	$("#friend_id").text(data["band_id"]);
	$("#friend_tel").text(data["telephone"]);
	$("#friend_email").text(data["email"]);
	$("#friend_fb").text(data["facebook"]);
})
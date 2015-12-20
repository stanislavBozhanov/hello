$('.my-form').submit(function(e){
	var url = "";

    $.ajax({
           type: "PUT",
           url: url,
           data: $(".my-form").serialize(), 
           success: function(data)
           {
               console.log(data); 
           }
         });
    // e.preventDefault();
})
$(document).ready(function(){
	//$("form#main_input_box").submit(function(event){
	//	event.preventDefault();
	//	var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
	//	var editButton = "<button class='edit btn btn-success'>Edit</button>";
	//	var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
	//	var checkBox = "<div class='checkbox'><label><input type='checkbox' class='pull-right'></label></div>";
	//	$(".list_of_items").append("<li class='list-group-item'>" + "<div class='text_holder'>" + $("#custom_textbox").val() + twoButtons + "</div>" + checkBox + "</li>");
	//	$("#custom_textbox").val('');
	//});

	//$(".list_of_items").on("click", "button.delete", function(){
	//	$(this).closest("li").remove();
	//});

	$(".list_of_items").on("click", "button.edit", function (){

        //var editid = $(this).siblings().attr("href");
        ////var editid = "/index/delitelist/3/";
        ////alert(editid);
        //var rep=editid.split("/");
        ////alert(rep[3]);
        //var editItemBox = "<form class='edit_input_box' action='/edittodo/' method='post' ><input type='text' class='itembox' name='editname'>" +
        //    "<a href=\"/index/edit/"+rep[3]+
        //    "\" title='edit'>"+
        //    "<input type='submit' value='submit' class='edit btn btn-success'></a></form>";
        //var editItemBox = "<form class='edit_input_box'><input type='text' class='itembox'><input type='submit' value='submit' class='edit btn btn-success'></form>";

        //var editItemBox = "<form class='edit_input_box'><input type='text' class='itembox'></form>";
		//var originalItem = $(this).parent().val();
		//var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		//var editButton = "<button class='edit btn btn-success'>Edit</button>";
		//var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
        ////alert(originalItem);
        //
		//$(this).closest("div.text_holder").replaceWith(editItemBox);
		//$("form.edit_input_box ").on("submit", function(){
		//	event.preventDefault();
		//	var checkBox = "<label><input type='checkbox'></label>";
		//	$(this).replaceWith("<div>" + $(".itembox").val() + twoButtons + "</div>");
         //   //window.location.href=$(this).closest("a").attr("href");
        //
		//});
	});
	
	$(".list_of_items").on("click", ":checkbox", function (){
		//$(this).closest("li").toggleClass("completed_item");
        window.location.href=$(this).closest("a").attr("href");
        //alert($(this).closest("a").attr("href"));
        //alert($(this).closest("label").closest("a").attr("href")) ;
        //window.location.href='http://www.baidu.com'
	});
    //$("submit").on("click", ":checkbox", function (){
	//	$(this).closest("li").toggleClass("completed_item");
	//});





});




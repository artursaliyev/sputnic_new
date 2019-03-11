var search = $(".form-control").val();


$(".col-12 p").each(function() {
    var text = $(this).text();
    // text = $.trim(text).substr(text.indexOf(search)-300, 600).split(" ").slice(0,-1).join(" ") + "...";
    console.log(text);
    var regex = new RegExp(search,'i');
    text = text.replace(regex, "<span class='yellow'>"+search+"</span>");
    $(this).html(text);

});
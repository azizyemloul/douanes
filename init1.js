// we will add our javascript code here
function recherche_code(){

    $("#ajax-code-form").submit(function(){

	var str = $(this).serialize();

	$.ajax({
	    type: "POST",
	    url: "rechercher.php",
	    data: str,

	    success: function(msg){

		$("#note").ajaxComplete(function(event, request, settings){

		    if(msg == 'OK') // Message Sent? Show the 'Thank You' message and hide the form
		    {
			result = '<div class="notification_ok">OK</div>';
			//$("#fields").hide();
		    }
		    else
		    {
			result = msg;
		    }

		    $(this).html(result);

		});

	    }

	});

	return false;

    });
    $("#ajax-code-form").submit();
};

//---------------------------------------------------------------------------

function showHint(num, str1,str2,str3)
{
    var xmlhttp;
    if (str1.length==0)
    {
	document.getElementById(num).innerHTML="";
	return;
    }
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
	xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
	xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
	if (xmlhttp.readyState==4 && xmlhttp.status==200)
	{
	    document.getElementById(num).innerHTML=xmlhttp.responseText;
	}
    }
    xmlhttp.open("GET","get_content.php?c="+str1+"&c2="+str2+"&c3="+str3,true);
    xmlhttp.send();
}

//--------------------------------------------------------------------------

function validate(evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode( key );
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
	theEvent.returnValue = false;
	theEvent.preventDefault();
    }
}

//---------------------------------------
function togle_frais(num){
    if(num=="maritime")
	document.getElementById("fraist").style.display="block";
    else document.getElementById("fraist").style.display="none";
}

//---------------------------------------
function togle_avantages(num){
    if(num=="1")
	document.getElementById("tauxi").style.display="block";
    else document.getElementById("tauxi").style.display="none";
}

//---------------------------------------
function get_cont(elmnt,id_chapitre, id_section, id_sous_section, id_article){
    var xmlhttp;
    if ((id_chapitre.length==0)&&(id_section.length==0)&&(id_sous_section.length==0)&&(id_article.length==0))
    {
	document.getElementById(elmnt).innerHTML="";
	return;
    }
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
	xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
	xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
	if (xmlhttp.readyState==4 && xmlhttp.status==200)
	{
	    document.getElementById(elmnt).innerHTML=xmlhttp.responseText;
	}
    }
    //xmlhttp.open("GET","get_content.php?id_chapitre="+id_chapitre+"&id_section="+id_section+"&id_sous_section="+id_sous_section+"&id_article="+id_article",true);
    //xmlhttp.open("GET","get_chapitre.php?id_chapitre="+id_chapitre,true);
    xmlhttp.open("GET","get_content.php?id_chapitre="+id_chapitre+"&id_section="+id_section+"&id_sous_section="+id_sous_section+"&id_article="+id_article,true);
    xmlhttp.send();
}

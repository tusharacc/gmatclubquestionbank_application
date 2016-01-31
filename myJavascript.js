

function checkTheAnswer () {
	var myOptionButton = document.getElementsByName("optradio");
	var optionSelected;

	for(var i = 0; i < myOptionButton.length; i++) {
   		if(myOptionButton[i].checked == true) {
       		optionSelected = myOptionButton[i].value;
   		}
 	}

 	//When answer is correct, make background as Green otherwise make it red
	if (optionSelected == answer.replace("\n","").replace("\t","").trim()){
		document.getElementById("answerOption").innerHTML = answer.replace("\n","").replace("\t","").trim();
		document.getElementById("buttonForEvaluation").setAttribute("style", "background-color:#99ff99");
		document.getElementById("questionblock").setAttribute("style", "background-color:#99ff99");
		document.getElementById("btnGetAnotherQuestion").disabled = false;
	} else {
		document.getElementById("buttonForEvaluation").setAttribute("style", "background-color:#ff6666");
		document.getElementById("questionblock").setAttribute("style", "background-color:#ff6666");
		document.getElementById("btnGetAnotherQuestion").disabled = false;
		document.getElementById("answerOption").innerHTML = answer.replace("\n","").replace("\t","").trim();

	}


}

function setTheSection (sectionTypeObj) {
	sectionTypeValue = sectionTypeObj.value;
	document.getElementById("complexityDropDown").disabled = false;

}

function displayQuestion(json){

	var rand = Math.random();
	console.log(rand);

	randNum = Math.floor(rand * json.length);
    console.log(randNum);
    question = json[randNum].question;
    console.log(question);
    answer = json[randNum].answer;
    used = json[randNum].used;

    if (used == 'Yes'){
    	var questionNotFound = true;
    	while (questionNotFound){
    		randNum = Math.floor(Math.random() * json.length);
    		answer = json[randNum].answer;
    		used = json[randNum].used;

    		if (used == 'No'){
    			questionNotFound = false;
    			var node = document.createElement("DIV");
		    	node.innerHTML = json[randNum].question;
		    	//var textnode = document.createTextNode(json[randNum].question);
		    	//node.appendChild(textnode);
		    	document.getElementById("question").appendChild(node);
		    	document.getElementById("questionblock").setAttribute("style", "display:block");
		    	document.getElementById("buttonForEvaluation").setAttribute("style", "display:block");
    		}

    	}
    } else {
    	var node = document.createElement("DIV");
    	node.setAttribute("id","questionDiv");
    	node.innerHTML = json[randNum].question;
    	//var textnode = document.createTextNode(json[randNum].question);
    	//node.appendChild(textnode);
    	document.getElementById("question").appendChild(node);
    	document.getElementById("questionblock").setAttribute("style", "display:block");
    	document.getElementById("buttonForEvaluation").setAttribute("style", "display:block");
    }
}

function getTheQuestion (dropdown) {

	var selectedValue = sectionTypeValue;
	var complexity = dropdown.value;
	var evaluationButtonAttribute = document.getElementById("buttonForEvaluation").hasAttribute("style");
	var questionBlockAttribute = document.getElementById("questionblock").hasAttribute("style");

	if (document.getElementById("question").hasChildNodes()){
		document.getElementById("question").removeChild(document.getElementById("questionDiv"));
		document.getElementById("answerOption").innerHTML = "";
	}

	if (questionBlockAttribute) {
		document.getElementById("questionblock").removeAttribute("style");
	}

	if (evaluationButtonAttribute) {
		document.getElementById("buttonForEvaluation").removeAttribute("style");
	}

	switch (selectedValue) {
		case "CR":
			if (complexity == 'high'){
				displayQuestion(CRJSON_HIGH);
			} else if (complexity == 'low') {
				displayQuestion(CRJSON_LOW)
			} else if (complexity == 'medium') {
				displayQuestion(CRJSON_MEDIUM)
			} else {
				alert ("Something went wrong. ")
			}
			break;
		case "SC":
			if (complexity == 'high'){
				displayQuestion(SCJSON_HIGH);
			} else if (complexity == 'low') {
				displayQuestion(SCJSON_LOW)
			} else if (complexity == 'medium') {
				displayQuestion(SCJSON_MEDIUM)
			} else {
				alert ("Something went wrong. ")
			}
			break;
			break;
		default:
			alert("Sorry!! Only CR & SC are set up");
			break;
	}

}


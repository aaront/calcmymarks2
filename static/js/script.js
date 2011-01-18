/* -----------------------------------------------------------------------

  CalcMyMarks Scripts
  http://calcmymarks.appspot.com

   * Copyright (c) 2009-2010 by Aaron Toth. See LICENSE for more info.

----------------------------------------------------------------------- */

var counter = 1;
var limit = 20;
var min = 0;
function addInput(divName){
     if (counter == limit)  {
          alert("You have reached the limit of adding " + counter + " term marks.");
     }
     else {
          var newdiv = document.createElement('div');
          newdiv.className = "curr_array";
          newdiv.innerHTML = "\
					<p>I have <input type='text' name='curr' class='inputbox' size='3'>%\
          on <input type='text' name='eval' class='inputbox' size='12'>\
					worth <input type='text' name='tally' class='inputbox' size='3'>% of the course.</p>";
          document.getElementById(divName).appendChild(newdiv);
          counter++;
     }
}

function removeInput(divName) {
    if (counter <= 1)  {
          alert("You have to at least have 1 term mark!");
    }
    else {
        var d = document.getElementById(divName);
        d.removeChild(d.lastChild);
        counter--;
    }
}

function clickclear(thisfield, defaulttext) {
    if (thisfield.value == defaulttext) {
        thisfield.value = "";
    }
}

function clickrecall(thisfield, defaulttext) {
    if (thisfield.value == "") {
        thisfield.value = defaulttext;
    }
}

function clearPaper(paper) {
    var paperDom = paper.canvas;
    paperDom.parentNode.removeChild(paperDom);
}

var r = Raphael("holder");

load_graph = function (tally, eval) {
    r.clear();
    r.g.txtattr.font = "16px/2em 'Droid Sans', Helvetica, Arial, sans-serif";
    var pie = r.g.piechart(80, 80, 70, tally, {legend: eval, legendpos: "east"});
};



$(function() {
    $('a#reset').bind('click', function() {
      window.location.reload()
    });

    $('a#calculate').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_calculate',
      $('#calcmarks').serialize(),
      function(data) {
        if(data.error)
        {
          alert("Obviously something was wrong with your attempt.\n\nTry again.\n\nMake sure there are no empty fields, and make sure you only enter in numbers for the percentages.");
          return;
        }
        $("#results").fadeIn();
        $("#result").text(data.res + '%');
        $("#result_str_1").text(data.res_str[0]);
        $("#result_str_2").text(data.res_str[1]);
        tally = data.tally;
        eval = data.eval;
        
        $('a#calculate').html('<span><span class="embolden">Re-calculate</span></span>');
        load_graph(data.tally, data.eval);

        $('html, body').animate({scrollTop: $("#top").offset().top},'slow');
      });
      return false;
    });
  });


function handleClick_carrello(cb) {
  var form = document.getElementById('Form');
  var controls = form.elements;

  for (var i=0; i<controls.length; i++) {
      if(controls[i].checked){
      document.getElementById('elimina').disabled = false;
      return
    }
  }
  document.getElementById('elimina').disabled = true;
}


function handleClick_home(cb) {
      var form = document.getElementById('Form');
      var controls = form.elements;

      for (var i=0; i<controls.length; i++) {
          if(controls[i].checked){
          document.getElementById('aggiungi').disabled = false;
          return
        }
      }
      document.getElementById('aggiungi').disabled = true;
  }
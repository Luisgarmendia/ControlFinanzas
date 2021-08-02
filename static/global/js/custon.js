$(()=>{
    $('.dropdown-trigger').dropdown();
    $('table').DataTable({});
    $('input:text').keydown(
        function (event){
            var letters = /^[A-Za-z]+$/;
            if(event.key.match(letters))
              {
               return true;
              }
            else
              {
              alert("message");
              return false;
              }
        }
    )
})


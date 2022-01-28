// Now When the page is ready the function will call
$(document).ready(function() {

    // First we will check the page is for add option or edit option or page reload


    // Page reload  on add page
    try{
        if($('[id="id_main_category"]')[0].value && !$('[id="id_category"]')[0].value){
            change($('[id="id_main_category"]')[0].value)
        }

    }catch{

    }

    // Edit Page
    try{
        if($('[id="id_main_category"]')[0].value && $('[id="id_category"]')[0].value){
            // then we will call the edit function
            edit($('[id="id_main_category"]')[0].value,$('[id="id_category"]')[0].value)
        }
    }catch{

    }

});


// This is will listen whenever the select option is change
document.addEventListener('change', function(event){
        let id = event.srcElement.id;  /// this will return us the id where select is change

        let value = event.target.value; // this will return the value of select change

        if(id === 'id_main_category' && value){  /// id_main_category is field or you can use id_your_field_name

            change(value)  // then we will call the select change fucntion
        }

})


// Select Change Function On Add Page
function change(value){
    var url = '/api/category/?main_category=' + value // Your API URL

    // then we will call ajax request.

    $.ajax({
      url: url,
      success: function (data) {

        // now we will get data and we have top map or loop it in options
          var html = $.map(data, function(data){
            return '<option value="' + data.id + '">' + data.name + '</option>'
        }).join('');
        html = '<option value selected>---------</option>' + html
        $("#id_category").html(html); // this will change the subcategory options
      }
    });
}


// Select Change Function On Edit Page
function edit(value, sub_value){
    var url = '/api/category/?main_category=' + value  // Your API URL
    // then we will call ajax request.
    $.ajax({
      url: url,
      success: function (data) {
         // now we will get data and we have top map or loop it in options
          var html = $.map(data, function(data){
            return '<option value="' + data.id + '">' + data.name + '</option>'
        }).join('');
        html = '<option value selected>---------</option>' + html
        $("#id_category").html(html); // this will change the subcategory options



        $("#id_category").val(sub_value);  // this will select the value of suncategory
      }
    });
}
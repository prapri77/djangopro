$('#form').find('input, textarea').on('keyup blur focus', function (e) {
  
    var $this = $(this),
        label = $this.prev('label');
  
        if (e.type === 'keyup') {
              if ($this.val() === '') {
            label.removeClass('active highlight');
          } else {
            label.addClass('active highlight');
          }
      } else if (e.type === 'blur') {
          if( $this.val() === '' ) {
              label.removeClass('active highlight'); 
              } else {
              label.removeClass('highlight');   
              }   
      } else if (e.type === 'focus') {
        
        if( $this.val() === '' ) {
              label.removeClass('highlight'); 
              } 
        else if( $this.val() !== '' ) {
              label.addClass('highlight');
              }
      }
  
  });
  
  $('.tab a').on('click', function (e) {
    
    e.preventDefault();
    
    $(this).parent().addClass('active');
    $(this).parent().siblings().removeClass('active');
    
    target = $(this).attr('href');
  
    $('.tab-content > div').not(target).hide();
    
    $(target).fadeIn(800);
    
  });

  // this for success page

  // $(function() {
  $("#submit").click(function() {
    window.open("payment_calculations_new.php","_self");
    
  });
  $("#edit").click(function() {
    // window.open("forms.php","_self");
    $("#input_1").submit();
  });
  // });

  $("#payment_proceed").click(function() {
    window.open("repayment_calculations.php","_self");
  });
  function verify_payment(payment_id, t_application_id){
    $("#loading").show();
    $.ajax({
      url : "ajax.php",
      async : true,
      type : 'POST',
      cache : false,
      data : {
        action : "verify_payment",
        t_application_id : t_application_id,
        payment_id : payment_id
      },
      success : function(response) {
        alert(response);
        location.reload();
        $("#loading").hide();
      }
    });

  }
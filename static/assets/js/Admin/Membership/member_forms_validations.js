var MemberFormValidation = function() {
    // Init Bootstrap Forms Validation, for more examples you can check out https://github.com/jzaefferer/jquery-validation
    var initValidationBootstrap = function(){
        jQuery('.js-validation-bootstrap').validate({
            ignore: ['cancel'],
            errorClass: 'help-block animated fadeInDown',
            errorElement: 'div',
            errorPlacement: function(error, e) {
                jQuery(e).parents('.form-group > div').append(error);
            },
            highlight: function(e) {
                var elem = jQuery(e);

                elem.closest('.form-group').removeClass('has-error').addClass('has-error');
                elem.closest('.help-block').remove();
            },
            success: function(e) {
                var elem = jQuery(e);

                elem.closest('.form-group').removeClass('has-error');
                elem.closest('.help-block').remove();
            },
            rules: {
                'name': {
                    required: true,
                    maxlength: 200
                },
                'surname': {
                    required: true,
                    maxlength:200
                },
                'dni': {
                    required: true                    
                },                                
                'address': {
                    required: true,
                    maxlength:200
                },
                'phone': {
                    required: true,
                    minlength:7
                    
                },
                'email': {
                    required: true,
                    email: true
                }
            },
            messages: {
                'name': {
                    required: 'Por favor ingrese un nombre',
                    maxlength: 'El nombre no puede tener más de 200 caracteres'
                },
                'surname': {
                    required: 'Por favor ingrese un apellido',                    
                    maxlength: 'El apellido no puede tener más de 200 caracteres'
                },
                'dni': {
                    required: 'Por favor ingrese un dni'                    
                },                
                'address': {
                    required: 'Por favor ingrese una dirección',
                    maxlength: 'La dirección no puede tener más de 200 caracteres'
                },
                'phone': {
                    required: 'Por favor ingrese un teléfono',   
                    minlength:'El telefono deber tener más de 6 digitos'                 
                },
                
                'email': {
                    required:'Por favor ingrese un email',
                    email:'Por favor ingrese un email válido'                
                }                
            }
        });
    };

    return {
        init: function () {
            // Init Bootstrap Forms Validation
            initValidationBootstrap();

            // Init Validation on Select2 change
            jQuery('.js-select2').on('change', function(){
                jQuery(this).valid();
            });
        }
    };
}();

// Initialize when page loads
jQuery(function(){ MemberFormValidation.init(); });

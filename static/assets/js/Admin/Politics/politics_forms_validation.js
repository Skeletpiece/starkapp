var ProviderFormValidation = function() {
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
                    required  : true,
                    maxlength : 40
                },
                'value': {
                    required  : true,
                    maxlength : 5,
                    number    : true,
                    min       : 0
                },
            },
            messages: {
                'name': {
                    required  : 'Por favor ingrese un Nombre',
                    maxlength : 'Por favor ingrese maximo 40 caracteres',
                },
                'value': {
                    required  : 'Por favor ingrese un precio',
                    maxlength : 'Por favor ingrese maximo 5 dígitos',
                    number    : 'Por favor ingrese solo números',
                    min       : 'Por favor ingrese un numero positivo'
                },

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
jQuery(function(){ ProviderFormValidation.init(); });

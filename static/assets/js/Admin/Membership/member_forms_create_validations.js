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
                'paternalLastName': {
                    required: true,
                    maxlength:200
                },
                'maternalLastName': {
                    required: true,
                    maxlength:200
                },
                'num_doc': {
                    required: true,   
                    number: true, 
                    min: 1,            
                },                              
                'address': {
                    required: true,
                    maxlength:200
                },
                'department': {
                     required: true,                             
                },  
                 'province': {
                     required: true,                           
                },  
                 'district': {
                     required: true,                           
                },  
                'phone': {
                    required: true,
                    number: true, 
                    minlength:7,
                    min:1
                    
                },
                'email': {
                    required: true,
                    email: true
                },
                'initialDate': {
                    required: true
                },
                'finalDate':{
                    required:true
                },
                'gender':{
                    required:true
                },
                'nationality':{
                    required:true,
                    maxlength:20
                },
                'workPlace':{
                    required:true,
                    maxlength:200
                },
                'workPlaceJob':{
                    required:true,
                    maxlength:200   
                },
                'workPlacePhone':{
                    required:true,
                    number: true, 
                    minlength:7
                },
                'maritalStatus':{
                    required:true,
                    maxlength:20  
                },
                'cellphoneNumber':{
                    required:true,
                    number: true, 
                    minlength:9
                },                
                'specialization':{
                    required:true,
                    maxlength:200  
                },
                'birthDate' : {
                    required: true
                },
                'birthPlace': {
                    required: true,
                    maxlength:200
                },                                                                
                'birthDepartment':{
                    required:true
                },
                'birthProvince':{
                    required:true
                },
                'birthDistrict':{
                    required:true
                },
                'photo':{
                    required:true
                }

            },
            messages: {
                'name': {
                    required: 'Por favor ingrese un nombre',
                    maxlength: 'El nombre no puede tener más de 200 caracteres'
                },
                'paternalLastName': {
                    required: 'Por favor ingrese un apellido',
                    maxlength: 'El apellido debe tener máximo 200 caracteres'                    
                },
                'maternalLastName': {
                    required: 'Por favor ingrese un apellido',
                    maxlength: 'El apellido debe tener máximo 200 caracteres'                    
                },
                'num_doc': {
                    required: 'Por favor ingrese un número de documento' ,
                    number: 'Por favor ingrese un documento válido' ,
                    min: 'Por favor ingrese un documento válido' ,                
                },              
                'address': {
                    required: 'Por favor ingrese una dirección',
                    maxlength: 'La dirección no puede tener más de 200 caracteres'
                },
                'department': {
                     required: "Por favor seleccione un departamento",                             
                },  
                 'province': {
                     required: "Por favor seleccione una provincia",                           
                },  
                 'district': {
                     required: "Por favor seleccione un distrito",                           
                },
                'phone': {
                    required: 'Por favor ingrese un teléfono',   
                    number: 'Por favor ingrese un número válido' ,
                    minlength:'El telefono deber tener más de 6 digitos',
                    min: 'Por favor ingrese un telefono válido'                  
                },
                
                'email': {
                    required:'Por favor ingrese un email',
                    email:'Por favor ingrese un email válido'                
                },
                'initialDate': {
                    required: 'Por favor ingrese una fecha inicial'
                },
                'finalDate':{
                    required: 'Por favor ingrese una fech final'
                },
                'birthDepartment':{
                    required:'Por favor ingrese un departamento'
                },
                'birthProvince':{
                    required:'Por favor ingrese una provincia'
                },
                'birthDistrict':{
                    required:'Por favor ingrese un distrito'
                },
                'specialization':{
                    required:'Por favor ingrese una especialización',
                    maxlength:'La especialización debe tener máximo 200 caracteres'  
                },
                'birthDate' : {
                    required: 'Por favor ingrese la fecha de nacimiento'
                },
                'birthPlace': {
                    required: 'Por favor ingrese un lugar de nacimiento',
                    maxlength:'El lugar de nacimiento debe tener máximo 200 caracteres'
                },
                'nationality':{
                    required:'Por favor ingrese una nacionalidad',
                    maxlength:'La nacionalidad debe tener máximo 20 caracteres'
                },
                'workPlace':{
                    required:'Por favor ingrese su centro de trabajo',
                    maxlength:'El centro de trabajo debe tener máximo 200 caracteres'
                },
                'workPlaceJob':{
                    required:'Por favor ingrese su puesto de trabajo',
                    maxlength:'El puesto de trabajo debe tener máximo 200 caracteres'
                },
                'workPlacePhone':{
                    required:'Por favor ingrese el teléfono del lugar de trabajo',   
                    number: 'Por favor ingrese un número válido' ,
                    minlength:'El telefono deber tener más de 6 digitos'
                },
                'maritalStatus':{
                    required:'Por favor ingrese un estado civil',
                    maxlength:'El estado civil debe tener máximo 200 caracteres'  
                },
                'cellphoneNumber':{
                    required:'Por favor ingrese un número celular',   
                    number: 'Por favor ingrese un número válido' ,
                    minlength:'El número deber tener 9 digitos'
                },
                'photo':{
                    required: 'Por favor ingrese una foto'
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

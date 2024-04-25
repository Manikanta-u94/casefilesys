var login_img_paths;
function get_images() {
    $.ajax({
        type: 'GET',
        url: "/accounts/login/login_images/",
        success: function(data){
            console.log(data["images"])
            login_img_paths = data["images"];
            var log_img_path = data["header"]
            var log_name = data["names"]
            var log_subtitle = data["subtitle"]
            var logo_img = log_img_path
            var logo_img_section = '<div style="width: 100%; margin-top:41px;" class="d-flex justify-content-center">  <img class="logo" src="'+logo_img+'" width="155" style="margin-top:-50px;margin-bottom:20px"> </div>'
            $(".login-left1").append(logo_img_section);

            var login_images = '<div class="owl-carousel owl-theme">'
            for (var i = 0; i < login_img_paths.length; i++) {
                if(i == 0){
                    login_images += '<div class="item active">'
                }else{
                    login_images += '<div class="item">'
                }
                
                login_images += '<div style="position:relative"><div style="position: absolute; bottom: 10px; left: 10px;color: white; z-index: 9999999; text-align: left;">'
                if(log_name[i]){
                    login_images += '<div style="font-size: 12px; font-weight: 800;">'+log_name[i]+'</div>'
                }
                
                if(log_subtitle[i]){
                    login_images += '<div style="font-size: 10px; line-height: 15px;">'+log_subtitle[i]+'</div>'
                }

                var img = login_img_paths[i]
                login_images += ' </div><img style="width: 190px; height: 200px;" src="'+img+'" class="img-fluid mx-auto d-block" alt="Logo1"></div></div>'

            }
            login_images += '</div>'
            if(login_img_paths.length != 0){
                login_images += '<div class="owl-theme"><div class="owl-controls"><div class="custom-nav owl-nav"></div></div></div>'
            }
            $(".main-content").append(login_images);

            var policy_banner_content = data['policy_text']//"This site contains controlled unclassified information (CUI) categorized as export controlled technology and technical data.The CUI on this site is utilized by Valence Surface Technologies to meet product compliance and is restricted for export by the Arms Export Control Act (Title 22, U.S.C., Sec 2751 et seq.) or the Export Administration Act (Title 50, U.S.C., App. 24001-240). Individuals granted access to CUI via this site agree to abide by all U.S. Export Laws and Government Regulations. Violation of these laws are subject to severe criminal penalties."
            var policy_banner = '<center style="font-size: 10px; line-height: 14px; text-align: justify;padding: 30px 15px 15px 15px; margin-top:-15px;"><font color="#000"><b style="color:white;">'+policy_banner_content+'</b></font></center>'
            $(".policy_banner").append(policy_banner);

            var pol_right = '<font color="#fff"><b>'+policy_banner_content+'</b></font> '
            $(".policy_right").append(pol_right);
        },
        complete: function(){
            // console.log($);
            $('.main-content .owl-carousel').owlCarousel({
                items: 3,
                loop: true,
                margin: 10,
                nav: true,
                autoplay: true,
                autoplayTimeout: 3000,
                autoplayHoverPause: true,
                navText: [
                    '<i class="fa fa-angle-left" aria-hidden="true"></i>',
                    '<i class="fa fa-angle-right" aria-hidden="true"></i>'
                ],
                navContainer: '.main-content .custom-nav'
            });
            $(".play").on("click", function () {
                owl.trigger("play.owl.autoplay", [1000]);
            });
            $(".stop").on("click", function () {
                owl.trigger("stop.owl.autoplay");
            });
        },
        error:function(data){
            console.log("Server is error");
        }
      });
    
  }

get_images();

  

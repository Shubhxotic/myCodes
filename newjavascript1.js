/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



$(document).ready(function (){
    $('.jbutton').click(function (){
        $('#ColorDiv').css('background-color',this.innerHTML.toLowerCase());
    });
});
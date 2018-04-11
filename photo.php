<?php

$token = 'Your token';
$v_api = '5.65';

  $data = curl("https://api.vk.com/method/photos.getMessagesUploadServer", array(
                
                'access_token' => $token, 
                'v' => $v_api
        ));

        if($data) {
            $image_path = dirname(__FILE__).'./out.png';
            $post_data = array("file1" => '@'.$image_path);
            $getUrl = json_decode($data, true);
            $url = $getUrl['response']['upload_url'];
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $url);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
            $result = json_decode(curl_exec($ch),true);
            $upload = curl_exec( $ch );
	echo($upload);
?>

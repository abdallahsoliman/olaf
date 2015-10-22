package io.soliman.olaf;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.telephony.SmsMessage;
import android.util.Log;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

import java.util.ArrayList;
import java.util.List;

public class SMSReceiver extends BroadcastReceiver {
    public SMSReceiver() {
        final SmsManager sms = SmsManager.getDefault();

        // setup http post request for api login
        HttpClient httpClient = new DefaultHttpClient();
        HttpPost loginPost = new HttpPost("http://localhost:8000/api/messages/");
    }

    @Override
    public void onReceive(Context context, Intent intent) {

        final Bundle bundle = intent.getExtras();

        try {
            if (bundle != null) {
                final Object[] pdusObj = (Object[]) bundle.get("pdus");

                for (int i = 0; i < pdusObj.length; i++) {

                    SmsMessage msg = SmsMessage.createFromPdu((byte[]) pdusObj[i]);
                    String senderNum = msg.getDisplayOriginatingAddress();
                    String msgBody = msg.getDisplayMessageBody();

                    List<NameValuePair> sms = new ArrayList<NameValuePair>(2);
                    sms.add(new BasicNameValuePair("sender", senderNum));
                    sms.add(new BasicNameValuePair("message", msgBody));


                    Log.i("SMSReceiver", "Sender: " + senderNum + "; msg: " + msgBody);


                }
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}

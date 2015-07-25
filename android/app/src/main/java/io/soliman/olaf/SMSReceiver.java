package io.soliman.olaf;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.telephony.SmsMessage;
import android.util.Log;

public class SMSReceiver extends BroadcastReceiver {
    public SMSReceiver() {
        final SmsManager sms = SmsManager.getDefault();
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

                    Log.i("SMSReceiver", "Sender: " + senderNum + "; msg: " + msgBody);
                }
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}

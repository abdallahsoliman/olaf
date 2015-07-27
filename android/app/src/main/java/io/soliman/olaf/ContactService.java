package io.soliman.olaf;

import android.app.IntentService;
import android.content.ContentResolver;
import android.content.Intent;
import android.content.Context;
import android.database.Cursor;
import android.net.Uri;
import android.provider.ContactsContract;

import java.net.URI;

/**
 * An {@link IntentService} subclass for handling asynchronous task requests in
 * a service on a separate handler thread.
 * <p/>
 * TODO: Customize class - update intent actions, extra parameters and static
 * helper methods.
 */
public class ContactService extends IntentService {

    // IntentService can perform, e.g. ACTION_FETCH_NEW_ITEMS
    private static final String ACTION_UPLOAD_CONTACTS = "io.soliman.olaf.action.UPLOAD_CONTACTS";
    private static final String ACTION_RESOLVE_CONTACT = "io.soliman.olaf.action.RESOLVE_CONTACT";

    /**
     * Starts this service to perform action Upload Contacts with the given parameters. If
     * the service is already performing a task this action will be queued.
     *
     * @see IntentService
     */
    // TODO: Customize helper method
    public static void startActionUploadContacts(Context context) {
        Intent intent = new Intent(context, ContactService.class);
        intent.setAction(ACTION_UPLOAD_CONTACTS);
        context.startService(intent);
    }

    public ContactService() {
        super("ContactService");
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        if (intent != null) {
            final String action = intent.getAction();
            if (ACTION_UPLOAD_CONTACTS.equals(action)) {
                handleActionUploadContacts();
            }
        }
    }

    /**
     * Handle action UploadContacts in the provided background thread
     */
    private void handleActionUploadContacts() {
        Uri CONTENT_URI = ContactsContract.Contacts.CONTENT_URI;
        Uri PHONE_CONTENT_URI = ContactsContract.CommonDataKinds.Phone.CONTENT_URI;

        String DISPLAY_NAME = ContactsContract.Contacts.DISPLAY_NAME;
        String HAS_PHONE_NUMBER = ContactsContract.Contacts.HAS_PHONE_NUMBER;
        String ID = ContactsContract.Contacts._ID;
        String PHONE_CONTACT_ID = ContactsContract.CommonDataKinds.Phone.CONTACT_ID;
        String NUMBER = ContactsContract.CommonDataKinds.Phone.NUMBER;

        ContentResolver contentResolver = getContentResolver();
        Cursor cursor = contentResolver.query(CONTENT_URI, null, null, null, null);

        if (cursor.getCount() > 0) {
            while (cursor.moveToNext()) {
                String name = cursor.getString(cursor.getColumnIndex(DISPLAY_NAME));
                String contactID = cursor.getString(cursor.getColumnIndex(ID));
                int hasPhoneNumber = Integer.parseInt(cursor.getString(cursor.getColumnIndex(HAS_PHONE_NUMBER)));


                if (hasPhoneNumber > 0) {
                    Cursor phoneCursor = contentResolver.query(
                            PHONE_CONTENT_URI, null,
                            String.format("%s = ?", PHONE_CONTACT_ID), new String[] {contactID}, null);

                    while (phoneCursor.moveToNext()) {
                        String phoneNumber = phoneCursor.getString(phoneCursor.getColumnIndex(NUMBER));
                        phoneCursor.close();
                    }
                }
            }
            cursor.close();
        }
    }
}

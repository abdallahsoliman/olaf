package io.soliman.olaf;

import android.content.Context;
import android.content.SharedPreferences;
import android.util.Log;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by soliman on 7/27/15.
 */
public class API {

    private HttpClient httpClient;
    private String rootUrl;
    private Context context;
    private SharedPreferences sharedSettings;
    private SharedPreferences.Editor sharedSettingsEditor;

    public API(Context context) {
        this.context = context;
        httpClient = new DefaultHttpClient();
        rootUrl = context.getString(R.string.root_api_url);
        sharedSettings = context.getSharedPreferences(
                context.getString(R.string.shared_preferences_file_key), Context.MODE_PRIVATE);
        sharedSettingsEditor = sharedSettings.edit();
    }

    public boolean login(String username, String password) {

        // setup http post request for api login
        HttpPost loginPost = new HttpPost(String.format(
                "http://%s%s", rootUrl, context.getString(R.string.login_path)
        ));

        // create post data using authentication credentials
        List<NameValuePair> loginCredentials = new ArrayList<NameValuePair>(2);
        loginCredentials.add(new BasicNameValuePair("username", username));
        loginCredentials.add(new BasicNameValuePair("password", password));

        try {
            loginPost.setEntity(new UrlEncodedFormEntity(loginCredentials));
            HttpResponse response = httpClient.execute(loginPost);
            JSONObject jsonResponse = new JSONObject(EntityUtils.toString(response.getEntity()));

            // save token in shared preferences
            sharedSettingsEditor.putString(
                    context.getString(R.string.sp_auth_token_key), jsonResponse.getString("token"));
            sharedSettingsEditor.apply();

            return true;
        }
        catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    public boolean isLoggedIn() {
        String token = getAuthToken();
        if (token != null) {
            Log.i("Authentication", "already authorized");
            return true;
        }
        else
            return false;
    }

    public boolean createContact(String name, String number) {
        HttpPost contactCreatePost = new HttpPost(String.format(
                "http://%s%s", rootUrl, context.getString(R.string.contact_path)
        ));
        contactCreatePost.addHeader("Authorization", String.format("Token %s", getAuthToken()));

        List<NameValuePair> contact = new ArrayList<NameValuePair>(1);
        contact.add(new BasicNameValuePair("name", name));
        contact.add(new BasicNameValuePair("number", number));

        try {
            contactCreatePost.setEntity(new UrlEncodedFormEntity(contact));
            HttpResponse response = httpClient.execute(contactCreatePost);

            if (response.getEntity() != null)
                response.getEntity().consumeContent();

            Log.i("\nContact Create", String.format("%s - %s: %s", name, number, response.getStatusLine().toString()));
            return true;
        }
        catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    public String getAuthToken() {
        return sharedSettings.getString(context.getString(R.string.sp_auth_token_key), null);
    }
}

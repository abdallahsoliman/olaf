package io.soliman.olaf;

import android.annotation.TargetApi;
import android.app.Activity;
import android.app.AlertDialog;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.content.Context;
import android.content.DialogInterface;
import android.content.pm.PackageManager;
import android.content.res.Configuration;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.preference.*;
import android.text.TextUtils;
import android.util.Log;


import java.util.List;
import java.util.prefs.PreferenceChangeListener;

/**
 * A {@link PreferenceActivity} that presents a set of application settings. On
 * handset devices, settings are presented as a single list. On tablets,
 * settings are split by category, with category headers shown to the left of
 * the list of settings.
 * <p/>
 * See <a href="http://developer.android.com/design/patterns/settings.html">
 * Android Design: Settings</a> for design guidelines and the <a
 * href="http://developer.android.com/guide/topics/ui/settings.html">Settings
 * API Guide</a> for more information on developing a Settings UI.
 */
public class SettingsActivity extends PreferenceActivity {
    /**
     * Determines whether to always show the simplified settings UI, where
     * settings are presented in a single list. When false, settings are shown
     * as a master/detail two-pane view on tablets. When true, a single pane is
     * shown on tablets.
     */
    private static final boolean ALWAYS_SIMPLE_PREFS = false;


    @Override
    protected void onPostCreate(Bundle savedInstanceState) {
        super.onPostCreate(savedInstanceState);

        FragmentManager mFragmentManager = getFragmentManager();
        FragmentTransaction mFragmentTransaction = mFragmentManager.beginTransaction();
        GeneralPreferenceFragment generalPreferenceFragment = new GeneralPreferenceFragment();
        mFragmentTransaction.replace(android.R.id.content, generalPreferenceFragment);
        mFragmentTransaction.commit();

    }

    public static class GeneralPreferenceFragment extends PreferenceFragment {

        Context context;

        @Override
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);

            this.context = getActivity();

            // Load the preferences from an XML resource
            addPreferencesFromResource(R.xml.pref_general);

            // bind listeners to their preferences
            bindToEnableServiceListener(findPreference("enable_sms_listener"));
            findPreference("resynchronize_contacts").setOnPreferenceClickListener(
                    new ResynchronizeContactListener(context));
        }
    }

    /**
     * A preference value change listener that toggles the corresponding service
     */
    private static Preference.OnPreferenceChangeListener enableServiceListener = new Preference.OnPreferenceChangeListener() {
        @Override
        public boolean onPreferenceChange(Preference preference, Object value) {

            if (preference instanceof CheckBoxPreference) {
                CheckBoxPreference checkBoxPreference = (CheckBoxPreference)preference;
                if (checkBoxPreference.getKey().equals("enable_sms_listener")) {
                    // TODO: toggle sms service
                }

            }
            return true;
        }
    };

    private static class ResynchronizeContactListener implements  Preference.OnPreferenceClickListener {

        Context context;

        public ResynchronizeContactListener(Context context) {
            this.context = context;
        }

        @Override
        public boolean onPreferenceClick(Preference preference) {

            new AlertDialog.Builder(context)
                .setTitle("Resynchronize Contacts")
                .setMessage("Are you sure you want to resynchronize your contacts?")
                .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        Log.i("Contact", "Resynchronization requested.");
                        ContactService.startActionUploadContacts(context);
                    }
                })
                .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        // do nothing
                    }
                })
                .setIcon(android.R.drawable.ic_dialog_alert)
                .show();

            return true;
        }
    }


    private static void bindToEnableServiceListener(Preference preference) {
        // Set the listener to watch for value changes.
        preference.setOnPreferenceChangeListener(enableServiceListener);
    }
}

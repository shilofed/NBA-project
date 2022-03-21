package com.example.a2_screens

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.*
import android.widget.AdapterView.OnItemClickListener

import android.widget.AutoCompleteTextView




class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // get reference to the string array that we just created
        val preferences = resources.getStringArray(R.array.types_of_game)
        // create an array adapter and pass the required parameter
        // in our case pass the context, drop down layout ,and array.
        val arrayAdapter = ArrayAdapter(this, R.layout.dropdown_item, preferences)
        // get reference to the autocomplete text view
//        val autocompleteTV = findViewById<AutoCompleteTextView>(R.id.autoCompleteTextView)
        // set adapter to the autocomplete tv to the arrayAdapter
//        autocompleteTV.setAdapter(arrayAdapter)
//        var preference = "none"
        var arg = ""
        for (pref in resources.getStringArray(R.array.types_of_game)){
            val curPref=intent.getIntExtra(pref, 5)
            arg = "$arg$pref=$curPref;"
        }

//        autocompleteTV.onItemClickListener =
//            OnItemClickListener { adapterView, view, position, id ->
////                preference = arrayAdapter.getItem(position).toString()
//            }

        val rollButton: Button = findViewById(R.id.button)
        rollButton.setOnClickListener{
            switchToGameRecScreen(rollButton, arg)
        }
        val prefButton: Button = findViewById(R.id.pref_button)
        prefButton.setOnClickListener{
            switchToPrefScreen(prefButton)
        }
    }

    fun switchToGameRecScreen(view: View, preference : String){
        val intent = Intent(this, DisplayMassageActivity::class.java)
        intent.putExtra("preference", preference)
        startActivity(intent)
    }

    fun switchToPrefScreen(view: View){
        val intent = Intent(this@MainActivity, Preference::class.java)
//        intent.putExtra("preference", preference)
        startActivity(intent)
    }

}
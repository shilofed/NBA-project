package com.example.a2_screens

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import com.example.a2_screens.data.Datasource
import io.ktor.client.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import okhttp3.*
import okhttp3.internal.wait
import okio.IOException
import org.json.JSONObject
import kotlin.concurrent.thread


class DisplayMassageActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_display_massage)
        val goBackButton: Button = findViewById(R.id.go_back_button)
        goBackButton.setOnClickListener() {
            go_back()
        }
        val userPreference=intent.getStringExtra("preference")
        if (userPreference != null) {
            get_data(userPreference)
        }
        else{
            get_data("")
        }
    }

    fun go_back() {
        val intent = Intent(this, MainActivity::class.java)
        startActivity(intent)
    }


    fun get_data(userPreference: String) {

        val request = Request.Builder()
//            .url("http://192.168.1.14:5000/")
            .url("http://10.100.102.23:5000/$userPreference")
            .build()

        val client = OkHttpClient()
        val call: Call = client.newCall(request)
        val thread: Thread = thread(start = true) {

            val response: Response = call.execute()
            val responseString: String = response.body!!.string()
            val jsonObj = JSONObject(responseString)

            if (!response.isSuccessful) throw IOException("Unexpected code $response")

            if (jsonObj["response_tag"] == 1) {
                try {
                    synchronized(this) {
                        runOnUiThread {
                            val team_1_logo: ImageView = findViewById(R.id.team_1_logo)
                            val team_2_logo: ImageView = findViewById(R.id.team_2_logo)
                            val team_1_name: TextView = findViewById(R.id.team_1_name)
                            val team_2_name: TextView = findViewById(R.id.team_2_name)
                            val teamsMap = Datasource().loadTeams()
                            val team1 = teamsMap[jsonObj["team_1_id"]]
                            val team2 = teamsMap[jsonObj["team_2_id"]]
                            if (team1 != null && team2 != null) {
                                team_1_logo.setImageResource(team1.logo)
                                team_1_name.setText(team1.name)
                                team_2_logo.setImageResource(team2.logo)
                                team_2_name.setText(team2.name)
                            }

                        }
                    }
                } catch (e: InterruptedException) {
                    e.printStackTrace()
                }
            }

        }


    }
}

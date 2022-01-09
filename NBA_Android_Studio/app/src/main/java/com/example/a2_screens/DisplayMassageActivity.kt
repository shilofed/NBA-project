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

        get_data2()

    }

    fun go_back() {
        val intent = Intent(this, MainActivity::class.java)
        startActivity(intent)
    }

    fun get_data() {

        val request = Request.Builder()
            .url("http://192.168.0.101:5000/")
            .build()

        val client = OkHttpClient()
        val call: Call = client.newCall(request)

        call.enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                e.printStackTrace()
            }

            override fun onResponse(call: Call, response: Response) {
                response.use {
                    if (!response.isSuccessful) throw IOException("Unexpected code $response")
                    try {
                        synchronized(this) {
                            runOnUiThread {
                                val responseString: String = response.body!!.string()
                                val jsonObj = JSONObject(responseString)
                                if (jsonObj["response_tag"] == 1) {
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
                        }
                    } catch (e: InterruptedException) {
                        e.printStackTrace()
                    }
                }
            }

        })
    }

    fun get_data2() {

        val request = Request.Builder()
            .url("http://192.168.0.101:5000/")
            .build()

        val client = OkHttpClient()
        val call: Call = client.newCall(request)
        println("${Thread.currentThread()} has run.")
        val thread: Thread = thread(start = true) {
            println("${Thread.currentThread()} has run.")
            val response: Response = call.execute()
            if (!response.isSuccessful) throw IOException("Unexpected code $response")
            try {
                synchronized(this) {
                    runOnUiThread {
                        val responseString: String = response.body!!.string()
                        val jsonObj = JSONObject(responseString)
                        if (jsonObj["response_tag"] == 1) {
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
                }
            } catch (e: InterruptedException) {
                e.printStackTrace()
            }

        }


    }
}

import { useStore } from "@nanostores/react";
import { useEffect, useRef, useState } from "react"
import { FaPlay, FaStop } from "react-icons/fa6";
import { $exercises, $plan, $pose_info } from "../stores/global";

export default function Feed() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [mediaStream, setMediaStream] = useState<MediaStream | null>(null);
  const [socket, setSocket] = useState<WebSocket | null>(null);
  const [points, setPoints] = useState<[number, number][]>([]);
  const [timer, setTimer] = useState(20);
  const [curr, setCurr] = useState(0);
  const plan = useStore($plan);
  
  const exerciseName = plan.exercise_program[curr].exercise;
  const info = $pose_info.get()[exerciseName.toLowerCase()]
  // console.log(exerciseName.toLowerCase())
  // convert to first letter capital

  const startWebcam = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
      }
      setMediaStream(stream);
      console.log("Joining stream", { stream });
    } catch (error) {
      console.error("Error accessing webcam", error);
    }
  };
  const stopWebcam = async () => {
    if (mediaStream) {
      mediaStream.getTracks().forEach((track) => {
        console.log("Stopping track", { track })
        track.stop();
      });
      setMediaStream(null);
    }
    setPoints([])
  };

  useEffect(() => {
    const countdown = setInterval(() => {
      if (timer <= 0) {
        setTimer(10);
        if (curr === plan.exercise_program.length - 1) {
          setCurr(0);
        } else {
          setCurr(curr + 1)
        }
      } else {
        setTimer(timer - 1)
      }
    }, 1000)
    return () => clearInterval(countdown)
  }, [timer, curr])

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/feed");
    ws.onopen = () => console.log("WebSocket connection opened");
    ws.onclose = () => console.log("WebSocket connection closed");
    ws.onerror = (error) => console.error("WebSocket error", error);
    ws.onmessage = (event) => {
      const playMessage = async (message: string) => {
        console.log("Playing message", { message });
        const utterance = new SpeechSynthesisUtterance(message);
        utterance.lang = "en-US";
        const voice = speechSynthesis.getVoices().find((voice) => voice.name === "Google US English");
        if (voice) utterance.voice = voice;
        speechSynthesis.speak(utterance);
      }
      // playMessage();
      const data = JSON.parse(event.data);
      if (data.feedback !== null) playMessage(data.feedback);
      setPoints(data.coords);
    }
    setSocket(ws);

    return () => ws.close();
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      if (!socket) return;
      if (socket.readyState !== WebSocket.OPEN) return;
      if (!mediaStream) return;
      if (!canvasRef.current) return;
      if (!videoRef.current) return;

      const video = videoRef.current;
      const canvas = canvasRef.current;
      const context = canvas.getContext("2d");

      if (!context) return;
      if (!video.videoWidth) return;
      if (!video.videoHeight) return;

      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      const data = canvas.toDataURL("image/jpeg");
      socket.send(JSON.stringify({ data, pose: exerciseName.toLowerCase() }));
    }, 1000 / 10);
    return () => clearInterval(interval);
  }, [mediaStream, socket, exerciseName])

  return (
    <div className="h-dvh w-full bg-snow flex items-center justify-center relative">
      <div className="flex flex-col gap-2 items-center">
        <div className="h-[550px] aspect-[4/3] relative">
          <video
            ref={videoRef}
            autoPlay
            muted
            className="border-4 border-neutral-400 rounded-3xl aspect-[4/3] bg-black"
            style={{ width: "100%" }}
          />
          {points.map((point, i) => {
            // console.log(`${(480 - point[1]) * 550}px`, `${(640 - point[0]) * (550 * 4/3)}px`)
            return (
              <div 
                key={i}
                className="w-6 h-6 rounded-full bg-pink-600 opacity-60 absolute"
                style={{ top: `${(point[1] / 480) * 550}px`, left: `${(point[0] / 640) * (550 * 4/3)}px` }}
              />
            )
          })}
          <canvas ref={canvasRef} className="hidden" />
        </div>
        <div className="flex gap-x-2">
          <button
            className="p-3 rounded-full bg-neutral-800 hover:bg-neutral-600 transition-colors"
            onClick={startWebcam}
          >
            <FaPlay className="text-snow" />
          </button>
          <button
            className="p-3 rounded-full bg-neutral-800 hover:bg-neutral-600 transition-colors"
            onClick={stopWebcam}
          >
            <FaStop className="text-snow" />
          </button>
        </div>
      </div>
      <div className="absolute top-8 left-8">
        <div className="h-32 aspect-square bg-darkoak rounded-full flex items-center justify-center text-beige font-lusitana text-4xl">
          {timer}
        </div>
        <h1>{plan.exercise_program[curr].exercise}</h1>
        <p className="max-w-64">{info.instructions}</p>
        <img src={`./poses/${info.image}`} className="w-64" />
      </div>
    </div>
  )
}
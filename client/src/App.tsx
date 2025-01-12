import { useStore } from "@nanostores/react"
import { $screen } from "./stores/global"
import Feed from "./screens/Feed";
import Form from "./screens/Form";
import Landing from "./screens/Landing";
import Debrief from "./screens/Debrief";

function App() {
  const screen = useStore($screen);

  return (
    <div className="h-dvh w-full bg-beige flex">
      {screen === "landing" && <Landing />}
      {screen === "form" && <Form />}
      {screen === "debrief" && <Debrief />}
      {screen === "feed" && <Feed />}
    </div>
  )
}

export default App
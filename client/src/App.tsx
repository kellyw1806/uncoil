import { useStore } from "@nanostores/react"
import { $screen } from "./stores/global"
import Landing from "./screens/Landing";

function App() {
  const screen = useStore($screen);

  return (
    <div className="h-dvh w-full bg-beige flex">
      {screen === "landing" && <Landing />}
    </div>
  )
}

export default App
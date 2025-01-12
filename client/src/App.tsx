import Feed from "./testing/Feed"
import Fetch from "./testing/Fetch"

function App() {


  return (
    <div className="h-dvh w-full p-4 grid grid-cols-2">
      <Fetch />
      <Feed />
    </div>
  )
}

export default App
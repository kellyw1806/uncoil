import Coil from "../components/Coil";
import { $screen } from "../stores/global";

export default function Landing() {
  return (
    <div className="h-dvh w-full flex relative">
      <img src="./landing/background.jpg" className="h-full w-full object-cover" />
      <div className="absolute top-0 right-0 h-full w-1/3 bg-[#000000A0] flex flex-col items-center justify-center">
        <div className="flex flex-col gap-y-6">
          <div className="mx-8">
            <div className="flex">
              <h1 className="text-pinenut text-6xl font-lusitana-bold">uncoil</h1>
              <div className="w-1 h-full relative">
                <Coil className="absolute left-[-8px] top-3 w-28 stroke-pinenut" />
              </div>
            </div>
            <h2 className="text-pinenut text-2xl font-lusitana-bold">the future of physiotherapy</h2>
          </div>
          <div className="w-full aspect-square relative flex flex-col items-center justify-center text-4xl font-lusitana">
            <div className="absolute top-0 left-0 bg-pinenut w-[85%] aspect-square rounded-full opacity-70" />
            <div className="absolute bottom-0 right-0 bg-sawdust w-[85%] aspect-square rounded-full opacity-70" />
            <p className="z-20">stretch.</p>
            <p className="z-20">correct.</p>
            <p className="z-20">relief.</p>
          </div>
          <div className="flex justify-center">
            <button
              className="bg-pinenut70 w-auto px-12 py-4 rounded-2xl text-xl font-lusitana text-beige hover:bg-pinenut transition-colors"
              onClick={() => $screen.set("form")}
            >
              Begin your journey!
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

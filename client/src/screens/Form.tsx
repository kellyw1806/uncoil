export default function Form() {
    return (
      <div className="h-dvh w-full bg-beige flex">
        <div className="h-full w-[600px] ml-40 relative">
          <img src="./landing.png" className="h-full object-cover" />
          <div className="absolute left-8 top-8 text-4xl">
            <h2 className="font-lusitana">stretch.</h2>
            <h2 className="font-lusitana">correct.</h2>
            <h2 className="font-lusitana">relief.</h2>
          </div>
        </div>
        <div className="flex-1 flex flex-col items-center justify-center gap-y-8">
          <div>
            <div className="flex">
              <h1 className="text-7xl text-center font-lusitana">uncoil</h1>
              <img src="./coil.svg" className="scale-75 mb-2" />
            </div>
            <h2 className="text-center text-2xl font-cedarville">
              the future of physiotherapy
            </h2>
          </div>
  
          <div className="flex flex-col items-center gap-y-4">
            <div className="bg-latte h-56 aspect-square rounded-full border-[12px] border-wood flex items-center justify-center">
              <div className="text-3xl m-4 font-serif ml-[1.75rem] text-beige">
                heal in the comfort of your home
              </div>
            </div>
            <div className="bg-wood h-12 aspect-square rounded-full" />
            <div className="bg-wood h-8 aspect-square rounded-full" />
          </div>
  
          <button className="bg-ocean text-beige text-2xl font-lusitana py-2 px-4 rounded-xl shadow-lg hover:bg-[#295f7d] transition-colors">
            begin your journey
          </button>
        </div>
      </div>
    )
  }
  
import Head from 'next/head'

//Components
import Header from '../components/Header';
import Slider from '../components/Slider';
import Footer from '../components/Footer';

export default function Home() {
  return (
    <div>
      <Head>
        <title>ArrangeAll</title>
        <link rel="icon" href="" />
      </Head>

      <header className="header">
        <Header />
      </header>

      <div>
        <Slider />
      </div>

      <div>
        <Footer />
      </div>

  </div>
  )
}

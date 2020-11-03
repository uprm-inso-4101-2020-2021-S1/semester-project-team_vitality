import React, { useState, useEffect } from 'react';
import Head from 'next/head'
import APIClient from '../apiClient';

//Components
import Header from '../components/Header';
import Slider from '../components/Slider';
import Footer from '../components/Footer';

export default function Home() {
  const apiClient = new APIClient();

  apiClient.login();
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

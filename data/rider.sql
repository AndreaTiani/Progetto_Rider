--
-- PostgreSQL database dump
--

\restrict S10GFJ8ysuRGdxUzkx9nZxIk8tobwsOfeNPctpOJA8w5PUHlDEcy4VAWa00R61u

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

-- Started on 2026-06-08 16:35:08

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 16396)
-- Name: reviews; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reviews (
    id bigint NOT NULL,
    rider_id bigint,
    customer_name character varying,
    rating bigint,
    comment character varying
);


ALTER TABLE public.reviews OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16388)
-- Name: riders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.riders (
    id bigint NOT NULL,
    name character varying,
    vehicle character varying,
    total_deliveries bigint
);


ALTER TABLE public.riders OWNER TO postgres;

--
-- TOC entry 4862 (class 2606 OID 16403)
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (id);


--
-- TOC entry 4860 (class 2606 OID 16395)
-- Name: riders riders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.riders
    ADD CONSTRAINT riders_pkey PRIMARY KEY (id);


--
-- TOC entry 4863 (class 2606 OID 16404)
-- Name: reviews rider_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT rider_id FOREIGN KEY (rider_id) REFERENCES public.riders(id);


-- Completed on 2026-06-08 16:35:08

--
-- PostgreSQL database dump complete
--

\unrestrict S10GFJ8ysuRGdxUzkx9nZxIk8tobwsOfeNPctpOJA8w5PUHlDEcy4VAWa00R61u


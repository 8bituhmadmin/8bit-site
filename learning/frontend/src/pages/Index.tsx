import * as React from "react";
import { createRoot } from "react-dom/client";
import { useEffect, useState } from "react";
import LoadingImage from "../components/LoadingImage";
import "../styles/styles.css";

interface Tag {
  tag_name: string;
  color: string;
}
interface Section {}

interface Lesson {
  name: string;
  skills: string;
  image: string;
  description: string;
  slug: string;
  tags: Tag[];
  sections: Section[];
  core_lesson: boolean;
  required_lesson: boolean;
  extension_lesson: boolean;
}

const Index = () => {
  const [pageReady, setPageReady] = useState<boolean>(false);
  const [canMap, setCanMap] = useState<boolean>(false);
  const [lessonData, setLessonData] = useState<Lesson[]>([]);

  useEffect(() => {
    try {
      const lessons = (window as any).data as any;
      setLessonData(lessons);
      // lessons.forEach((lesson: any) => {
      //   console.log(lesson);
      // });

      setCanMap(true);
      setPageReady(true);
    } catch (e: any) {
      setPageReady(true);
    }
  }, []);
  return (
    <>
      <div
        className="container sm:mx-auto px-5 max-w-screen-xl"
        style={{ paddingTop: 100, paddingBottom: 100 }}
        data-aos="fade-up"
        data-aos-duration="1500"
      >
        {pageReady ? (
          <>
            {canMap ? (
              <>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                  {lessonData.map((lesson, key) => {
                    if (lesson.sections.length > 0) {
                      return (
                        <div
                          key={key}
                          className="bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
                        >
                          <a
                            href={`/learning/lessons/${lesson.slug}/1`}
                            className="mb-3"
                          >
                            <LoadingImage
                              imageUri={lesson.image}
                              className="img-fluid float-left rounded-t mb-3"
                            />
                          </a>
                          <div className="p-5">
                            <a href={`/learning/lessons/${lesson.slug}/1`}>
                              <h5 className="text-2xl font-bold text-gray-900 dark:text-white hover:underline">
                                {lesson.name}
                              </h5>
                            </a>
                            <div className="flex py-2 flex-wrap">
                              {lesson.required_lesson ? (
                                <span className="my-1 bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-lg dark:bg-red-900 dark:text-red-300">
                                  Required Lesson
                                </span>
                              ) : null}
                              {lesson.core_lesson ? (
                                <span className="my-1 bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-lg dark:bg-green-900 dark:text-green-300">
                                  Core Lesson
                                </span>
                              ) : null}
                              {lesson.tags.map((val, key) => {
                                return (
                                  <>
                                    <span
                                      key={key}
                                      className="my-1 bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-lg dark:bg-blue-900 dark:text-blue-300"
                                    >
                                      {val.tag_name}
                                    </span>
                                  </>
                                );
                              })}
                            </div>

                            <p className="font-normal text-gray-700 dark:text-gray-400">
                              {lesson.description}
                            </p>
                          </div>
                        </div>
                      );
                    }
                  })}
                </div>
              </>
            ) : (
              <div style={{ marginBottom: 700 }}>
                Uh oh! Something went wrong with our request for data. Please
                refresh and try again!
              </div>
            )}
          </>
        ) : (
          <div
            className="d-flex justify-content-center"
            style={{ marginBottom: 700 }}
          >
            <div className="spinner-border my-5"></div>
          </div>
        )}
      </div>
    </>
  );
};

const root = document.getElementById("page-root");
createRoot(root).render(<Index />);
